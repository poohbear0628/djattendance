// Class for managing the seating chart view for roll taking
// 
// Dependencies - jQuery, Grid.js
// 
// TODO - API to return all data we need in one ajax call 
//        based on event.id and date of event
//        This inlcudes chart, seat, section and trainee data

var SeatController = {
	// Variables
	trainees: [],
	chart: {},
	seats: [],
	sections: [],
	selected_sections: {},
	gender: "B",
	seat_grid: null,
	map: [],
	min_x: 0,
	min_y: 0,
	max_x: 0,
	max_y: 0,

	// Default options
	options: {
		section_button_div: "#buttons_section",

	},

	init: function (opts, trainees, chart, seats, sections){
		var t = SeatController;
		for (var k in opts){
			if(t.options[k] != null){
				t.options[k] = opts[k];
			}
		}

		t.trainees = trainees;
		t.chart = chart;
		t.seats = seats;
		t.sections = sections;

		t.create_section_buttons();
		t.build_grid();
		t.calculate_offest();

		return SeatController;
	},

	build_grid: function (){
		var t = SeatController;
		t.seat_grid = new Grid(t.chart.width, t.chart.height);
		for (var i = 0; i < t.seats.length; i++) {
			var pk = t.seats[i].trainee;
			t.seat_grid.grid[t.seats[i].y][t.seats[i].x].pk = pk;
			for (var j = 0; j < trainees.length; j++) {
				if (pk == trainees[j].id) {
					t.seat_grid.grid[t.seats[i].y][t.seats[i].x].name = t.trainees[j].firstname + ' ' + t.trainees[j].lastname;
					t.seat_grid.grid[t.seats[i].y][t.seats[i].x].current_term = t.trainees[j].current_term;
					t.seat_grid.grid[t.seats[i].y][t.seats[i].x].gender = t.trainees[j].gender;
				}
			}
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
				if(seat.name != null && seat.gender == t.gender){
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
					t.map[i] += "_";
				}
			}
		}
		t.draw();
	},

	calculate_offest: function (){
		var t = SeatController;
		$('#seat-map').empty();
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
		console.log(t.min_x, t.min_y, t.max_x, t.max_y);
		if(t.max_x > 0 && t.max_y > 0)
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
			).append('&nbsp;').append(
				$("<button>", {
					class: "btn",
				 	text: "Hide All",
				 	on: {
				 		click: t.onclick_hide_all
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
		t.calculate_offest();
	},

	onclick_hide_all: function (e){
		var t = SeatController;
		//Mark all buttons not selected
		$(".section-toggles").removeClass("btn-primary");
		for(var k in t.selected_sections){
			t.select_section(k, false, false);
		}
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
		console.log(t.gender);
		t.calculate_offest();
	},

	// This function is called when a change in the model happens
	// or when user selects a particular section of the grid
	draw: function (){
		// TODO - 
		var t = SeatController;

		var scObject = {
			map: t.map,
			seats: {},
			naming: {
				top: true,
				left: true,
			}
		}

		var sc = $('#seat-map').seatCharts(scObject);
		$("#seat-map").css("width", ((t.max_x+2)*60).toString() + "px");

		for (var i = t.min_y; i < t.max_y; i++) {
			for (var j = t.min_x; j < t.max_x; j++) {
				var id = (i+1-t.min_y) + '_' + (j+1-t.min_x);
				var seat = t.seat_grid.grid[i][j];
				if(seat.gender == t.gender){
					sc.get(id).node().text(seat.name);
				}
			}
		}
	}
}