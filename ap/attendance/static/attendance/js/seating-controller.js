// Class for managing the seating chart view for roll taking
//
// Dependencies - jQuery, Grid.js

const uniform_tardies_brothers = [
  "",
  "Bdg Flipped",
  "No Bdg",
  "Bdg Covered",
  "Top Button/Collar",
  "Tie",
  "Wrong Blazer",
  "Wrong Pants",
  "Wrong Socks",
  "Shoes"
];
const uniform_tardies_sisters = [
  "",
  "Bdg Flipped",
  "No Bdg",
  "Hair Over Bdg",
  "Bdg Covered",
  "Top Button/Collar",
  "Scarf Color",
  "No Sweater/Blazer",
  "Sweater Color",
  "Nylons",
  "Leggings",
  "Shoes"
];

const termClass = {
  1: "first-term",
  2: "second-term",
  3: "third-term",
  4: "fourth-term"
};

class SeatController {
  constructor (opts, trainees, chart, seats, sections, event, date, rolls, individualslips, groupslips){
    const t = this;

    // Default options
    const options = {
      section_button_div: "#buttons_section",
      url_rolls : "/api/rolls/"
    }
    t.options = Object.assign(options, opts)

    t.build_trainees(trainees, rolls, individualslips, groupslips);
    t.chart = chart;
    t.seats = seats;
    t.sections = sections;
    t.event = event;
    t.date = date;
    t.gender = "B";
    t.selected_sections = {};

    t.create_section_buttons();
    t.build_grid();
    t.calculate_offset(true);
    t.onclick_view_all();

    //Popover catch all
    $('body').off('shown.bs.popover').on('shown.bs.popover', e => {
      const elem = $(e.target);
      const rcpair = elem.attr('id').split('_');
      const row = rcpair[0] - 1;
      const column = rcpair[1] - 1;
      const popover = elem.data('bs.popover').$tip;
      const input = popover.find('textarea, select');

      input.focus();
      input.select();

    }).off('blur', '#seat-notes').on('blur', '#seat-notes', e => {
      const elem = $(e.target);
      const x = elem.data('x');
      const y = elem.data('y');
      const seat = t.seat_grid.grid[y][x];
      //Only update if new value.
      //This is to prevent uniform tardy from clearing the notes
      if(elem.val() != ""){
        seat.notes = elem.val();
        t.update_roll(seat, false);
      }
    });
  }

  build_trainees (jsonTrainees, jsonRolls, jsonIndividualSlips, jsonGroupSlips){
    const t = this;
    t.trainees = {};
    jsonTrainees.forEach(v => {
      t.trainees[v.id] = {
        ...v,
        pk: v.id,
        name: v.firstname + " " + v.lastname,
        term: v.current_term,
      }
    })
    jsonRolls.forEach(roll => {
      console.log(t.trainees[roll.trainee], roll);
      t.trainees[roll.trainee] = {
        ...roll,
        ...t.trainees[roll.trainee]
      }
      console.log(t.trainees[roll.trainee]);
    })
    //Add leaveslips to trainee
    jsonIndividualSlips.forEach(ls => t.trainees[ls.trainee].leaveslip = true)
    jsonGroupSlips.forEach(trainee => {
      if(t.trainees[trainee.id]){
        t.trainees[trainee.id].leaveslip = true;
      }
    })
  }

  build_grid (){
    const t = this;
    t.seat_grid = new Grid(t.chart.width, t.chart.height);
    t.seats
      .filter(seat => seat.x >= 0 && seat.y >= 0 && seat.x <= t.chart.width && seat.y <= t.chart.height)
      .forEach(seat => {
        t.seat_grid.grid[seat.y][seat.x] = {
          ...t.trainees[seat.trainee],
          ...seat,
        }
      })
  }

  // Builds map object to plug into seatCharts object
  build_map (){
    const t = this;
    t.map = new Grid(t.max_x-t.min_x, t.max_y-t.min_y);
    const seats = [].concat(...t.seat_grid.grid)
    seats
      .filter(seat => seat.gender == t.gender)
      .filter(seat => seat.x >= t.min_x && seat.y >= t.min_y && seat.x <= t.max_x && seat.y <= t.max_y)
      .forEach(seat => {
        t.map.grid[seat.y-t.min_y][seat.x-t.min_x] = seat
      })
    t.draw();
  }

  calculate_offset (changeSection){
    const t = this;
    if(changeSection){
      t.min_x = t.chart.width;
      t.min_y = t.chart.height;
      t.max_x = 0;
      t.max_y = 0;
      for(const k in t.selected_sections){
        const section = t.selected_sections[k]
        if(section.selected){
          if(section.min_x < t.min_x){
            t.min_x = section.min_x;
          }
          if(section.min_y < t.min_y){
            t.min_y = section.min_y;
          }
          if(section.max_x > t.max_x){
            t.max_x = section.max_x;
          }
          if(section.max_y > t.max_y){
            t.max_y = section.max_y;
          }
        }
      }
    }
    t.build_map();
  }

  // Creates button for sections
  create_section_buttons (){
    const t = this;
    t.sections.forEach(s => {
      t.selected_sections[s.section_name] = {
        selected: false,
        min_x: s.x_lower,
        min_y: s.y_lower,
        max_x: s.x_upper,
        max_y: s.y_upper
      };
      $(t.options.section_button_div).append(
        $("<button>", {
          class: "btn section-toggles",
          text: s.section_name,
          'data-section': s.section_name,
          on: {
            click: (e) => t.onclick_section_button(e)
          }
         })
      ).append('&nbsp;');
    })
    $(t.options.section_button_div).append('&nbsp;').append('&nbsp;').append(
      $("<button>", {
        class: "btn btn-primary",
        text: "View All",
        on: {
          click: (e) => t.onclick_view_all(e)
        }
       })
    );
  }

  isselect_section_button (btn){
    return btn.hasClass("btn-primary");;
  }

  // Onclick function for section button
  onclick_section_button (e){
    const t = this;
    const button = $(e.target);
    button.toggleClass("btn-primary");
    const selected = t.isselect_section_button(button);
    const section_name = button.data("section");
    // console.log(t.selected_sections);
    t.select_section(section_name, selected, true);
  }

  onclick_view_all (e){
    const t = this;
    //Mark all buttons selected
    $(".section-toggles").addClass("btn-primary");
    t.min_x = 0;
    t.min_y = 0;
    t.max_x = t.chart.width;
    t.max_y = t.chart.height;
    for(const section in t.selected_sections){
      t.select_section(section, true);
    }
    t.build_map();
  }

  onclick_hide_all (e){
    const t = this;
    //Mark all buttons not selected
    $(".section-toggles").removeClass("btn-primary");
    for(const k in t.selected_sections){
      t.select_section(k, false);
    }
  }

  onclick_seat (ev, elem){
    const t = this;
    const seat = t.get_seat_from_elem(elem)
    if(!seat.attending || seat.finalized){
      return;
    }
    //Update status
    switch(seat.status){
      case 'P':
        seat.status = 'A';
        break;
      case 'A':
        seat.status = 'U';
        break;
      case 'U':
        seat.status = 'T';
        break;
      case 'T':
        seat.status = 'L';
        break;
      case 'L':
        seat.status = 'P';
        break;
      default:
        seat.status = 'A';
    }
    t.update_roll(seat);
  }

  onrightclick_seat (ev, elem){
    const t = this;
    const seat = t.get_seat_from_elem(elem)
    if(!seat.attending || seat.finalized){
      return;
    }
    t.show_notes(seat);
  }

  get_seat_from_elem(elem){
    const t = this;
    const rc_list = elem.id.split('_');
    const y = parseInt(rc_list[0])+t.min_y-1;
    const x = parseInt(rc_list[1])+t.min_x-1;
    return t.seat_grid.grid[y][x];
  }

  show_notes (seat){
    const t = this;
    const x = seat.x;
    const y = seat.y;
    const elem = $("#"+(y+1-t.min_y)+"_"+(x+1-t.min_x));
    let content = "";
    if(seat.status == 'U'){
      content += '<select class="form-control" data-x="'+x+'" data-y="'+y+'" id="seat-notes">';
      uniform_tardies = (t.gender == "B")?uniform_tardies_brothers:uniform_tardies_sisters;
      uniform_tardies.forEach(e => {
        content += '<option value="'+uniform_tardies[k]+'"';
        if(seat.notes == uniform_tardies[k]){
          content += ' selected ';
        }
        const text = (e == '' ? 'Select Reason for U' : e);
        content += '>'+text+'</option>';
      })
      content += '</select>';
    } else {
      content += '<textarea class="form-control" data-x="'+x+'" data-y="'+y+'" id="seat-notes" placeholder="Enter Your Reason">'+seat.notes+'</textarea>';
    }
    t.popover = $(elem).popover({
      placement: 'right auto',
      trigger: 'manual',
      content: content,
      html: true
    }).popover('show');

    // Close popover onblur
    const popover = elem.data('bs.popover').$tip;
    const textarea = popover.find('textarea');
    textarea.on('blur', e => $(e.target).parent().parent().popover('destroy'));
  }

  onlongclick_seat (ev, elem){
    const t = this;
    t.onrightclick_seat(ev, elem);
  }

  onclick_finalize (e){
    const t = this;
    t.finalize_seats(true);
  }

  onclick_unfinalize (e){
    const t = this;
    t.finalize_seats(false);
  }

  finalize_seats (finalized=false){
    const t = this;

    const seats = [].concat(...t.map.grid)
    seats
      .filter(seat => seat.pk)
      .filter(seat => seat.attending)
      .forEach(seat => {
        seat.finalized = finalized;
        if(!seat.status){
          seat.status = "P";
        }
        t.update_roll(seat, true);
      })
  }

  update_roll(seat, finalize=false){
    const t = this;
    let data = {
      event: t.event.id,
      trainee: seat.id,
      status: seat.status,
      notes: seat.notes,
      date: t.date
    };
    t.update(seat);   // Draw optimistically to remove UI delay
    if(finalize)
      data.finalized = seat.finalized;
    $.ajax({
      type: "POST",
      url: t.options.url_rolls,
      data: data,
      success: function (response){
      	let seat = t.trainees[response.trainee];
      	// Check if response is newer and update accordingly
      	if(seat.last_modified < response.last_modified){
      		seat.last_modified = response.last_modified;
      		// Update seat status if different and update UI
      		if(seat.status != response.status){
      			seat.status = response.status;
      			t.update(seat);
      		}
      	}
      },
    });
  }

  select_section (section_name, selected, redraw=false){
    const t = this;
    t.selected_sections[section_name].selected = selected;
    if(redraw)
      t.calculate_offset(true);
  }

  toggle_gender (e){
    const t = this;
    t.gender = e.target.checked?"B":"S";
    t.calculate_offset(false);
  }

  //Tardy Color - #fc6
  //Absent Color - #e55

  // This function is called when a change in the model happens
  // or when user selects a particular section of the grid
  draw (){
    const t = this;

    const scObject = {
      map: t.map,
      hideEmptySeats: true,
      seats: {},
      click: (e, elem) => t.onclick_seat(e, elem),
      right_click: e => t.onrightclick_seat(e),
      tap_hold: e => t.onrightclick_seat(e),
      naming: {
        top: true,
        left: true,
      }
    }

    const sm = $("#seat-map");

    // clear map before redrawing
    sm.empty();
    if(t.max_x > 0 && t.max_y > 0){
      const sc = sm.seatCharts(scObject);
      sm.css("width", ((t.max_x+1)*60).toString() + "px");

      const seats = [].concat(...t.map.grid)
      seats
        .filter(seat => seat.pk)
        .forEach(seat => {
          const id = "#"+(seat.y+1-t.min_y) + '_' + (seat.x+1-t.min_x);
          const node = $(id);
          t.draw_node(node, seat)
        })
    }

    t.resize();
  }

  // Function to call to adjust width since we disable user zooming
  // in the FastClick library
  resize (){
    const sm = $("#seat-map");
    const body = $('body');
    const bw = body.get(0).scrollWidth;

    // Resize body if container width greater
    if (body.outerWidth() < bw) {
      body.width(bw);
    }

    if (body.height() < sm.height()) {
      body.height(sm.height());
    }
  }

  // Smarter draw function.. Instead of redrawing everything
  update (trainee){
  	const t = this;
    const x = trainee.x;
  	const y = trainee.y;
  	const id = "#"+(y+1-t.min_y) + '_' + (x+1-t.min_x);
    const seat = trainee;
    const node = $(id);
    // Destroy popover
    if(t.popover){
	    t.popover.popover('destroy');
    }
    t.draw_node(node, seat);

    //Show popover if uniform tardy
    if(trainee.status == 'U'){
      t.show_notes(seat, y, x);
    }
  }

  draw_node (node, seat){
    node.html("<b>"+seat.name+"</b>");
    node.attr('title', seat.notes);
    if(seat.attending){
    	node.removeClass('roll-absent uniform_tardies uniform roll-tardy left-class leaveslip');
    	if(seat.leaveslip){
    		node.addClass('leaveslip');
    	}
      if (seat.status != ''){
        node.removeClass('first-term second-term third-term fourth-term')
      }
      switch(seat.status){
        case 'A':
          node.addClass("roll-absent");
          break;
        case 'P':
          node.addClass(termClass[seat.term]);
          break;
        case 'U':
          node.addClass("roll-tardy uniform");
          break;
        case 'L':
          node.addClass("roll-tardy left-class");
          break;
        case 'T':
          node.addClass("roll-tardy");
          break;
      }
    } else {
      node.addClass('roll-disabled');
    }
    if(seat.finalized){
      node.addClass('finalized');
    } else {
    	node.removeClass('finalized');
    }
  }
}