// Class for managing the seating chart view for roll taking
// 
// Dependencies - jQuery, Grid.js

var uniform_tardies_brothers = [
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
var uniform_tardies_sisters = [
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

var uniform_tardies;

var SeatController = {
	// Variables
	trainees: {},
	chart: {},
	seats: [],
	sections: [],
	selected_sections: {},
	event: {},
	date: "",
	gender: "",
	seat_grid: null,
	map: null,
	min_x: 0,
	min_y: 0,
	max_x: 0,
	max_y: 0,
	popover: null,

	// Default options
	options: {
		section_button_div: "#buttons_section",
		url_rolls : "/api/rolls/"
	},

	init: function (opts, trainees, chart, seats, sections, event, date, rolls){
		var t = SeatController;
		for (var k in opts){
			if(t.options[k] != null){
				t.options[k] = opts[k];
			}
		}

		t.build_trainees(trainees, rolls);
		t.chart = chart;
		t.seats = seats;
		t.sections = sections;
		t.event = event;
		t.date = date;
		t.gender = "B";

		t.create_section_buttons();
		t.build_grid();
		t.calculate_offset(true);
		t.onclick_view_all();

		//Popover catch all
		$('body').off('shown.bs.popover').on('shown.bs.popover', function(e) {
			// console.log('popover shown', e);

			var elem = $(e.target);
			var rcpair = elem.attr('id').split('_');
			var row = rcpair[0] - 1;
			var column = rcpair[1] - 1;
			var popover = elem.data('bs.popover').$tip;
			var input = popover.find('textarea, select');

			input.focus();
			input.select();

		}).off('blur', '#seat-notes').on('blur', '#seat-notes', function(e) {
			var elem = $(e.target);
			var x = elem.data('x');
			var y = elem.data('y');
			var seat = t.seat_grid.grid[y][x];
			//Only update if new value. 
			//This is to prevent uniform tardy from clearing the notes
			if(elem.val() != ""){
				seat.notes = elem.val();
				t.update_roll(seat, false);
			}
			//t.popover.popover('destroy');
		});

		return SeatController;
	},

	build_trainees: function (jsonTrainees, jsonRolls){
		var t = SeatController;
		t.trainees = {};
		for(var i=0; i<jsonTrainees.length; i++){
			var trainee = jsonTrainees[i];
			var tid = trainee.id;
			t.trainees[tid] = trainee;
			t.trainees[tid].pk = trainee.id;
			t.trainees[tid].name = trainee.firstname + " " + trainee.lastname;
			t.trainees[tid].status = "";
			t.trainees[tid].notes = "";
			t.trainees[tid].attending = false;
		}
		for(var j=0; j<jsonRolls.length; j++){
			var roll = jsonRolls[j];
			t.trainees[roll.trainee].status = roll.status;
			t.trainees[roll.trainee].notes = roll.notes;
			t.trainees[roll.trainee].finalized = roll.finalized;
		}
	},

	build_grid: function (){
		var t = SeatController;
		t.seat_grid = new Grid(t.chart.width, t.chart.height);
		for (var i = 0; i < t.seats.length; i++) {
			var seats = t.seats[i];
			var x = parseInt(seats.x);
			var y = parseInt(seats.y);
			if(x < 0 || y < 0 || x > t.chart.width || y > t.chart.height)
				continue;
			t.trainees[seats.trainee].attending = seats.attending;
			t.seat_grid.grid[seats.y][seats.x] = t.trainees[seats.trainee];
		}
	},

	// Builds map object to plug into seatCharts object
	build_map: function (){
		var t = SeatController;
		t.map = new Grid(t.max_x-t.min_x, t.max_y-t.min_y);
		for (var i = 0; i < t.max_y-t.min_y; i++) {
			for(var j = 0; j < t.max_x-t.min_x; j++){
				if(t.seat_grid.grid[i+t.min_y][j+t.min_x].gender == t.gender){
					t.map.grid[i][j] = t.seat_grid.grid[i+t.min_y][j+t.min_x];
				}
			}
		}
		t.draw();
	},

	calculate_offset: function (changeSection){
		var t = SeatController;
		if(changeSection){
			t.min_x = t.chart.width;
			t.min_y = t.chart.height;
			t.max_x = 0;
			t.max_y = 0;
			for(var k in t.selected_sections){
				var selected_section = t.selected_sections[k];
				// console.log(selected_section);
				if(selected_section.selected){
					if(selected_section.min_x < t.min_x){
						t.min_x = selected_section.min_x;
					}
					if(selected_section.min_y < t.min_y){
						t.min_y = selected_section.min_y;
					}
					if(selected_section.max_x > t.max_x){
						t.max_x = selected_section.max_x;
					}
					if(selected_section.max_y > t.max_y){
						t.max_y = selected_section.max_y;
					}
				}
			}
		}
		t.build_map();
	},

	// Creates button for sections
	create_section_buttons: function (){
		var t = SeatController;
		t.selected_sections = {};
		for(var i=0; i<t.sections.length; i++){
			var section = t.sections[i];
			t.selected_sections[section.section_name] = {};
			var selected_section = t.selected_sections[section.section_name];
			selected_section.selected = false;
			selected_section.min_x = section.x_lower;
			selected_section.min_y = section.y_lower;
			selected_section.max_x = section.x_upper;
			selected_section.max_y = section.y_upper;
			$(t.options.section_button_div).append(
				$("<button>", {
					class: "btn section-toggles",
				 	text: section.section_name,
				 	'data-section': section.section_name,
				 	on: {
				 		click: t.onclick_section_button
				 	}
				 })
			).append('&nbsp;');
		}
		$(t.options.section_button_div).append('&nbsp;').append('&nbsp;').append(
			$("<button>", {
				class: "btn btn-primary",
			 	text: "View All",
			 	on: {
			 		click: t.onclick_view_all
			 	}
			 })
		);
	},

	isselect_section_button: function(btn){
		return btn.hasClass("btn-primary");;
	},
	// Onclick function for section button
	onclick_section_button: function (e){
		var t = SeatController;
		var button = $(e.target);
		button.toggleClass("btn-primary");
		var selected = t.isselect_section_button(button);
		var section_name = button.data("section");
		// console.log(t.selected_sections);
		t.select_section(section_name, selected, true);
	},

	onclick_view_all: function (e){
		var t = SeatController;
		//Mark all buttons selected
		$(".section-toggles").addClass("btn-primary");
		t.min_x = 0;
		t.min_y = 0;
		t.max_x = t.chart.width;
		t.max_y = t.chart.height;
		for(var k in t.selected_sections){
			t.select_section(k, true, false);
		}
		t.build_map();
	},

	onclick_hide_all: function (e){
		var t = SeatController;
		//Mark all buttons not selected
		$(".section-toggles").removeClass("btn-primary");
		for(var k in t.selected_sections){
			t.select_section(k, false, false);
		}
	},

	onclick_seat: function (ev, elem){
		var t = SeatController;
	    var rc_list = elem.id.split('_');
	    var y = parseInt(rc_list[0])+t.min_y-1;
	    var x = parseInt(rc_list[1])+t.min_x-1;

		// console.log(this, x,y);
		var seat = t.seat_grid.grid[y][x];
		var ATTENDANCE_TYPE = ['P','A','T','U','L'];
		if(!seat.attending || seat.finalized){
			return;
		}
		//Update status
		switch(seat.status){
			case 'P':
				seat.status = 'A';
				break;
			case 'A':
				seat.status = 'T';
				break;
			case 'T':
				seat.status = 'U';
				break;
			case 'U':
				seat.status = 'L';
				break;
			case 'L':
				seat.status = 'P';
				break;
			default:
				seat.status = 'A';
		}
		if(seat.status == 'U'){
			//If toggled to uniform tardy open the context menu
			t.draw();
			t.show_notes(seat, x, y);
		} else {
			t.update_roll(seat);
		}
	},

	onrightclick_seat: function (ev, elem){
		var t = SeatController;
		var rc_list = elem.id.split('_');
	    var y = parseInt(rc_list[0])+t.min_y-1;
	    var x = parseInt(rc_list[1])+t.min_x-1;
	    var seat = t.seat_grid.grid[y][x];
		if(!seat.attending || seat.finalized){
			return;
		}
		t.show_notes(seat, x, y);
	},

	show_notes: function (seat, x, y){
		var t = SeatController;
		var elem = $("#"+(y+1-t.min_y)+"_"+(x+1-t.min_x));
		if(seat.status == 'U'){
			var select_menu = '<select class="form-control" data-x="'+x+'" data-y="'+y+'" id="seat-notes">';
			uniform_tardies = (t.gender == "B")?uniform_tardies_brothers:uniform_tardies_sisters;
			for(var k = 0; k < uniform_tardies.length	; k++){
				select_menu += '<option value="'+uniform_tardies[k]+'"';
				if(seat.notes == uniform_tardies[k]){
					select_menu += ' selected ';
				}
				select_menu += '>'+uniform_tardies[k]+'</option>';
			}
			select_menu += '</select>';
			t.popover = $(elem).popover({
		      placement: 'right auto',
		      trigger: 'manual',
		      content: select_menu,
		      html: true
		    }).popover('show');
		} else {
			t.popover = $(elem).popover({
		      placement: 'right auto',
		      trigger: 'manual',
		      content: '<textarea class="form-control" data-x="'+x+'" data-y="'+y+'" id="seat-notes">'+seat.notes+'</textarea>',
		      html: true
		    }).popover('show');
		}
	},

	onlongclick_seat: function (ev, elem){
		var t = SeatController;
		t.onrightclick_seat(ev, elem);
	},

	onclick_finalize: function(e){
		var t = SeatController;
		
		for (var i = 0; i < t.map.height; i++) {
			for (var j = 0; j < t.map.width; j++) {
				var seat = t.map.grid[i][j];
				if(seat.gender == t.gender){
					if(seat.attending){
						seat.finalized = true;
						if(!seat.status){ //If no roll is set for current seat yet set Present as default
							seat.status = "P";
						}
						t.update_roll(seat, true);
					}
				}
			}
		}
	},

	onclick_unfinalize: function (e){
		var t = SeatController;
		
		for (var i = 0; i < t.map.height; i++) {
			for (var j = 0; j < t.map.width; j++) {
				var seat = t.map.grid[i][j];
				if(seat.gender == t.gender){
					if(seat.attending){
						seat.finalized = false;
						if(!seat.status){ //If no roll is set for current seat yet set Present as default
							seat.status = "P";
						}
						t.update_roll(seat, true);
					}
				}
			}
		}
	},

	update_roll: function(seat, finalize){
		var t = SeatController;
		var data = {};
		data.event = t.event.id;
		data.trainee = seat.id;
		data.status = seat.status;
		data.notes = seat.notes;
		data.date = t.date;
		if(finalize)
			data.finalized = seat.finalized;
		$.ajax({
			type: "POST",
			url: t.options.url_rolls,
			data: data,
			success: function (response){
				console.log(response);
				t.draw();
			},
		});
	},

	select_section: function (section_name, selected, redraw){
		var t = SeatController;
		
		t.selected_sections[section_name].selected = selected;
		if(redraw)
			t.calculate_offset(true);
	},

	toggle_gender: function (e){
		var t = SeatController;
		t.gender = e.target.checked?"B":"S";
		t.calculate_offset(false);
	},

	//Tardy Color - #fc6
	//Absent Color - #e55

	// This function is called when a change in the model happens
	// or when user selects a particular section of the grid
	draw: function (){
		var t = SeatController;

		var scObject = {
			map: t.map,
			hideEmptySeats: true,
			seats: {},
			click: t.onclick_seat,
			right_click: t.onrightclick_seat,
			tap_hold: t.onrightclick_seat,
			naming: {
				top: true,
				left: true,
			}
		}

		// clear map before redrawing
		$('#seat-map').empty();
		if(t.max_x > 0 && t.max_y > 0){
			var sc = $('#seat-map').seatCharts(scObject);
			$("#seat-map").css("width", ((t.max_x+2)*60).toString() + "px");
	
			for (var i = t.min_y; i < t.max_y; i++) {
				for (var j = t.min_x; j < t.max_x; j++) {
					var id = "#"+(i+1-t.min_y) + '_' + (j+1-t.min_x);
					var seat = t.seat_grid.grid[i][j];
					var node = $(id);
					if(node && seat){
						if(seat.gender == t.gender){
							node.html("<b>"+seat.name+"</b>");
							if(seat.attending){
								switch(seat.status){
									case 'A':
										node.addClass("roll-absent");
										break;
									case 'P':
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
							}
						}
					}
				}
			}
		}
	}
}