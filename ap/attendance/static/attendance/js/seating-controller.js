// Class for managing the seating chart view for roll taking
// 
// Dependencies - jQuery, Grid.js

var SeatController = {
	// Variables
	trainees: {},
	chart: {},
	seats: [],
	sections: [],
	selected_sections: {},
	event: {},
	date: "",
	gender: "B",
	seat_grid: null,
	map: [],
	min_x: 0,
	min_y: 0,
	max_x: 0,
	max_y: 0,
	finalized: true,

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

		t.create_section_buttons();
		t.build_grid();
		t.calculate_offest();

		return SeatController;
	},

	build_trainees: function (jsonTrainees, jsonRolls){
		var t = SeatController;
		t.trainees = {};
		for(var i=0; i<jsonTrainees.length; i++){
			var trainee = jsonTrainees[i];
			t.trainees[trainee.id] = trainee;
			t.trainees[trainee.id].name = trainee.firstname + " " + trainee.lastname;
			t.trainees[trainee.id].status = "";
			t.trainees[trainee.id].notes = "";
			t.trainees[trainee.id].attending = false;
		}
		for(var j=0; j<jsonRolls.length; j++){
			var roll = jsonRolls[j];
			t.trainees[roll.trainee].status = roll.status;
			t.trainees[roll.trainee].notes = roll.notes;
			t.trainees[roll.trainee].finalized = roll.finalized;
			if(!roll.finalized){
				t.finalized = false;
			}
		}
	},

	build_grid: function (){
		var t = SeatController;
		t.seat_grid = new Grid(t.chart.width, t.chart.height);
		for (var i = 0; i < t.seats.length; i++) {
			var seats = t.seats[i];
			t.trainees[seats.trainee].attending = seats.attending;
			t.seat_grid.grid[seats.y][seats.x] = t.trainees[seats.trainee];
		}
	},

	// Builds map object to plug into seatCharts object
	build_map: function (){
		var t = SeatController;
		t.map = [];
		for (var i = t.min_y; i < t.max_y; i++) {
			t.map[i] = "";
			for(var j=t.min_x; j<t.max_x; j++){
				var seat = t.seat_grid.grid[i][j];
				if(seat){
					if(seat.name != null && seat.gender == t.gender){
						if(seat.attending){
							switch (seat.current_term){
								case 1:
									t.map[i] += "a";
									break;
								case 2:
									t.map[i] += "b";
									break;
								case 3:
									t.map[i] += "c";
									break;
								case 4:
									t.map[i] += "d";
									break;
								default:
									t.map[i] += "a";
							}
						} else {
							t.map[i] += "D";
						}
					} else {
						t.map[i] += "_";
					}
				}
			}
		}
		t.draw();
	},

	calculate_offest: function (){
		var t = SeatController;
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
		t.build_map();
	},

	// When we get a list of new trainee objects
	// we update our list of current trainees
	// Maybe just write over current object instead of loop
	// for efficiency. then create another function to add individual
	update_trainees: function (){
		var t = SeatController;
	},

	// When chart updates we need to get new seats object
	// also update our trainees object
	update_chart: function (){

	},

	update_seats: function (){

	},

	// Update buttons for sections
	update_sections: function (){

	},

	// When we make the one ajax call with
	update_data: function (){

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
	// Onclick function for section button
	onclick_section_button: function (e){
		var t = SeatController;
		var button = $(e.target);
		button.toggleClass("btn-primary");
		var selected = button.hasClass("btn-primary");
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

	onclick_seat: function (){
		var t = SeatController;
		var seat_node = this.node; //The seat object that the library returns
		var y = parseInt(this.settings.row)+t.min_y;
		var x = parseInt(this.settings.column)+t.min_x;
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
		
		t.update_roll(seat);
	},

	onclick_finalize: function(e){
		var t = SeatController;
		
		for (var i = t.min_y; i < t.max_y; i++) {
			for (var j = t.min_x; j < t.max_x; j++) {
				var id = (i+1-t.min_y) + '_' + (j+1-t.min_x);
				var seat = t.seat_grid.grid[i][j];
				if(seat.gender == t.gender){
					seat.finalized = true;
					if(seat.attending){
						if(!seat.status){ //If no roll is set for current seat yet set Present as default
							seat.status = "P";
						}
						t.update_roll(seat, true);
					}
				}
			}
		}
		t.finalized = true;
	},

	onclick_unfinalize: function (e){
		var t = SeatController;
		
		for (var i = t.min_y; i < t.max_y; i++) {
			for (var j = t.min_x; j < t.max_x; j++) {
				var id = (i+1-t.min_y) + '_' + (j+1-t.min_x);
				var seat = t.seat_grid.grid[i][j];
				if(seat.gender == t.gender){
					seat.finalized = false;
					if(seat.attending){
						if(!seat.status){ //If no roll is set for current seat yet set Present as default
							seat.status = "P";
						}
						t.update_roll(seat, true);
					}
				}
			}
		}
		t.finalized = false;
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
			t.calculate_offest();
	},

	toggle_gender: function (e){
		var t = SeatController;
		t.gender = e.target.checked?"B":"S";
		t.build_map();
	},

	//Tardy Color - #fc6
	//Absent Color - #e55

	// This function is called when a change in the model happens
	// or when user selects a particular section of the grid
	draw: function (){
		var t = SeatController;

		var scObject = {
			map: t.map,
			seats: {},
			click: t.onclick_seat,
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
					var id = (i+1-t.min_y) + '_' + (j+1-t.min_x);
					var seat = t.seat_grid.grid[i][j];
					var node = sc.get(id);
					if(node && seat){
						node = node.node();
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