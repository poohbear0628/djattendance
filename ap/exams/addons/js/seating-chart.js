/* Seating Charts
 *
 * Author: David Schontzler
 *
 * Used for viewing/editing/entering roll data into seating charts.
**/

dojo.require("dojo.lang.*");
dojo.require("dojo.io.*");
dojo.require("dojo.event.*");
dojo.require("dojo.html.*");

/* SeatingChart
*****************************/
function SeatingChart(node) {
	this.container = dojo.byId(node);
	this.table = this.container.getElementsByTagName("table")[0];
	if(dojo.html.hasAttribute(this.container, "url")) {
		this.url = this.container.getAttribute("url");
	}
	this.seats = {};
	var se = this.table.getAttribute("seateditor");
	if(se) {
		this.seatEditor = new SeatEditor(se, this);
	}

	if(dojo.html.hasClass(this.container, "user")) {
		this.userMode();
	}

	if(dojo.html.hasClass(this.container, "locked")) {
		this.lock();
	}

	dojo.event.connect(this.table, "onclick", this, "onclick");
	dojo.event.connect(this.table, "ondblclick", this, "ondblclick");
        dojo.event.connect(this.table, "onmouseout", this, "onmouseout")//T.L. Keep

	// find existing seats
	for(var y = 0; y < this.table.rows.length; y++) {
		var cells = this.table.rows[y].cells;
		for(var x = 0; x < cells.length; x++) {
			var cell = cells[x];
			if(this.isSeat(cell)) {
				this.getSeat(cell); // creates a "Seat" obj
			}
		}
	}
}
dojo.lang.extend(SeatingChart, {
	table: null,
	seats: null,
	seatEditor: null,
	pad: 5,
	locked: false,
	mode: "seat", // or "user"
	url: "nowhere",
	content: null,
	dirty: false,
	_dataGrid: false,

	setDataGrid: function(grid) {
		this._dataGrid = grid;
	},

	clearSeats: function() {
		for(var id in this.seats)
			this.seats[id].setValue("");
		this.dirty = true;
	},

	getData: function() {
		var obj = {
			"seatId[]": [],
			"x[]": [],
			"y[]": [],
			"traineeId[]": []
		};
		for(var id in this.seats) {
			var seat = this.seats[id];
			if(!this.isSeat(seat.td)) {continue;}
			seat.update();

			obj["seatId[]"].push(seat.id);
			obj["x[]"].push(seat.x);
			obj["y[]"].push(seat.y);
			obj["traineeId[]"].push(seat.getTraineeID());
		}

		// normalize x & y coords
		var minX = Math.min.apply(this, obj["x[]"]);
		for(var i = 0; i < obj["x[]"].length; i++) {
			obj["x[]"][i] -= minX;
		}

		var minY = Math.min.apply(this, obj["y[]"]);
		for(var i = 0; i < obj["y[]"].length; i++) {
			obj["y[]"][i] -= minY;
		}

		return obj;
	},

	submit: function(asForm) {
		this.dirty = false;
		if(asForm) {
			if(!this.form) {
				this.form = document.createElement("form");
				this.form.method = "post";
				dojo.body().appendChild(this.form);
			}
			dojo.html.removeChildren(this.form);

			this.form.action = this.url;
			var data = dojo.lang.mixin(this.getData(), this.content);
			var input = document.createElement("input");
			input.type = "hidden";
			for(var key in data) {
				if(dojo.lang.isArrayLike(data[key])) {
					for(var i = 0; i < data[key].length; i++) {
						var entry = input.cloneNode(true);
						entry.name = key;
						entry.value = data[key][i];
						this.form.appendChild(entry);
					}
				} else {
					var entry = input.cloneNode(true);
					entry.name = key;
					entry.value = data[key];
					this.form.appendChild(entry);
				}
			}
			this.form.submit();
		} else {
			dojo.io.bind({
				url: this.url,
				method: "post",
				content: dojo.lang.mixin(this.getData(), this.content),
				handler: function(type, data, event) {
					if(type == "load") {
						//alert("Saved!");
					} else {
						//alert("Couldn't save");
					}
				}
			});
		}
	},

	setValue: function(seat, value) {
		if(arguments.length == 3) {
			var x = seat;
			var y = value;
			seat = this.table.rows[y].cells[x];
			value = arguments[2];
		}
		this.dirty = true;
	},

	isUserMode: function() {
		return this.mode == "user";
	},

	isSeatMode: function() {
		return this.mode == "seat";
	},

	userMode: function() {
		this.mode = "user";
		dojo.html.addClass(this.container, "user");
	},

	seatMode: function() {
		this.mode = "seat";
		dojo.html.removeClass(this.container, "user");
	},

	lock: function() {
		dojo.html.addClass(this.container, "locked");
		this.locked = true;
	},

	unlock: function() {
		dojo.html.removeClass(this.container, "locked");
		this.locked = false;
	},

	toggleLocked: function() {
		if(this.locked) {
			this.unlock();
		} else {
			this.lock();
		}
	},

	onclick: function(e) {//T.L. Keep
		var seat = dojo.html.isTag(e.target, "td") ? e.target
			: dojo.html.getParentByType(e.target, "td");

		if(seat) {
			if(!this.locked) {
				if(this.isSeatMode()) {
					if(!this.isSeat(seat)) {
						this.addSeat(seat);
					}
				} else if(this.isUserMode()) {
					if(this.isSeat(seat)) {
						this.editSeat(seat);
					}
				}
			} else if(this._dataGrid && this.isSeat(seat)) {
                                //Add the 'floating' class to the table of the dataGrid before showing the table next to the particular seat
                                if (this._dataGrid._mode == DataGrid._modes.FLOATING)
                                    dojo.html.addClass(this._dataGrid.table, "floating");
				var id = "row" + seat.id.substring("seat".length);
				this._dataGrid.filterAndPlace(id, e.pageX, e.pageY);
			}
		}
	},

        //To allow for the dataGrid to be modified both on a per seat basis and by having the entire dataGrid at once (it cannot be viewed in 
        //two places at once currently), every time there is a mouseout of the seating chart, repopulate the datagrid below
	onmouseout: function() {
		this._dataGrid.showAllRows();
	},

	ondblclick: function(e) {
		if(this.locked || !this.isSeatMode()) { return; }

		var seat = dojo.html.isTag(e.target, "td") ? e.target
			: dojo.html.getParentByType(e.target, "td");

		if(seat) {
			if(this.isSeat(seat)) {
				if(this.isOccupied(seat)) {
					if(confirm("This seat is taken, remove?")) {
						this.removeSeat(seat);
					}
				} else {
					this.removeSeat(seat);
				}
			}
		}
	},

	addSeat: function(seat) {
		if(this.locked || !this.isSeatMode()) { return; }

		var div = dojo.html.firstElement(seat);
		if(!dojo.html.hasClass(div, "seat")) {
			dojo.html.addClass(div, "seat");
			this.updateSize(seat);
			this.getSeat(seat);
		}
		this.dirty = true;
	},

	removeSeat: function(seat) {
		if(this.locked || !this.isSeatMode()) { return; }

		var div = dojo.html.firstElement(seat);
		if(dojo.html.hasClass(div, "seat")) {
			dojo.html.removeClass(div, "seat");
		} 
		//added lines to handle the different seat classes
		else if(dojo.html.hasClass(div, "secondSeat")) {
			dojo.html.removeClass(div, "secondSeat");
		} else 
		if(dojo.html.hasClass(div, "thirdSeat")) {
			dojo.html.removeClass(div, "thirdSeat");
		} else
		if(dojo.html.hasClass(div, "fourthSeat")) {
			dojo.html.removeClass(div, "fourthSeat");
		}
		//end added lines
		div.innerHTML = "";
		this.dirty = true;
	},

	getSeat: function(seat) {
		var id = seat.id;
		if(!id) {
			id = dojo.html.getUniqueId(); // PROBLEM!
// Unique ID has to be auto-generated by the MySQL auto-increment itself.
// Use a new ID of -2 to indicate that this ID should added to the
// database as a new Seat.
			seat.id = id;
		}

		if(!this.seats[id]) {
			this.seats[id] = new Seat(seat, this);
		}

		return this.seats[id];
	},

	editSeat: function(seat) {
		if(this.locked || !this.isUserMode()) {return;}
		if(!this.isSeat(seat)) {return;}

		var seat = this.getSeat(seat);
		seat.edit();
		this.dirty = true;
	},

	isSeat: function(td) {
		var div = dojo.html.firstElement(td);
		if((dojo.html.hasClass(div, "seat") || dojo.html.hasClass(div, "secondSeat")) ||
			(dojo.html.hasClass(div, "thirdSeat") || dojo.html.hasClass(div, "fourthSeat"))) {
			return true;
		} else {
			return false;
		}
	},

	isOccupied: function(td) {
		return this.isSeat(td) && Boolean((this.getSeat(td)||{}).trainee);
	},
/*
	getTrainee: function(seat) {
		var div = dojo.html.firstElement(seat);
		var id = div.getAttribute("trainee");
		return Trainees[id];
	},
*/
	updateSize: function(td) {
		if(this.locked || !this.isSeatMode()) {return;}

		var x = td.cellIndex;
		var y = td.parentNode.rowIndex;

		var w = this.table.rows[0].cells.length;
		var h = this.table.rows.length;

		var pad = this.pad;

		if(x == 0) {
			this.createColumns(1, false);
		} else if(x + pad >= w) {
			this.createColumns(x + pad - w + 1, true);
		}

		if(y == 0) {
			this.createRows(1, false);
		} else if(y + pad >= h) {
			this.createRows(y + pad - h + 1, true);
		}
	},

	createColumns: function(num, atEnd) {
		if(this.locked || !this.isSeatMode()) { return; }

		for(var i = 0; i < num; i++) {
			this.createColumn(atEnd);
		}
	},

	createColumn: function(atEnd) {
		if(this.locked || !this.isSeatMode()) { return; }

		var td = document.createElement("td");
		td.innerHTML = "<div></div>";

		var rows = this.table.rows;
		for(var i = 0; i < rows.length; i++) {
			if(atEnd) {
				rows[i].appendChild(td.cloneNode(true));
			} else {
				rows[i].insertBefore(td.cloneNode(true), rows[i].firstChild);
			}
		}
		
		this.dirty = true;
	},

	createRows: function(num, atBottom) {
		if(this.locked || !this.isSeatMode()) {return;}

		for(var i = 0; i < num; i++) {
			this.createRow(atBottom);
		}
	},

	createRow: function(atBottom) {
		if(this.locked || !this.isSeatMode()) {return;}

		var tr = this.table.rows[0].cloneNode(true);
		dojo.lang.forEach(tr.getElementsByTagName("td"), function(td) {
			td.id = "";
			td.innerHTML = "<div></div>";
		});

		if(atBottom) {
			dojo.html.insertAfter(tr, this.table.rows[this.table.rows.length-1]);
		} else {
			var row = this.table.rows[0];
			row.parentNode.insertBefore(tr, row);
		}
		
		this.dirty = true;
	}
});

/* Check for dirty...

window.onbeforeunload = function() {
	if(seatingChart1.dirty) {
		return "You haven't saved the seating chart!";
	}
}

*/

/* Seat
****************************/

function Seat(td, chart) {
	this.td = dojo.byId(td);
	this.chart = chart;
	this.div = dojo.html.firstElement(this.td);
	this.editor = chart.seatEditor;

	var id = this.div.getAttribute("seatid");
	//if(id) { this.trainee = Trainees[id]; }

	//id = this.div.getAttribute("seatid");
	if(id) { this.id = id; }

	this.update();
}
dojo.lang.extend(Seat, {
	x: -1,
	y: -1,
	id: 0,
	traineeID: null,
	traineeFirstName: null,
	traineeLastName: null,

	edit: function() {
		dojo.html.addClass(this.td, "editing");
		this.editor.setTraineeID(this.getTraineeID());
		this.editor.show(this);
		this.editor.onHide = dojo.lang.hitch(this, function() {
			dojo.html.removeClass(this.td, "editing");
		});
		this.editor.onSubmit = dojo.lang.hitch(this, function(value) {
			dojo.html.removeClass(this.td, "editing");
			this.setTrainee(this.editor.getTraineeID(),
				this.editor.getTraineeFirstName(),
				this.editor.getTraineeLastName(),
				this.editor.getTraineeTerm(),
                this.editor.getTraineeSendingLocality());
		});
	},
	
	setTrainee: function(traineeID, firstName, lastName, term, sendingLocality) {
		if(traineeID==null||traineeID==0) {
            this.traineeID=0;
  			this.traineeFirstName="";
  			this.traineeLastName="";
  			this.traineeSendingLocality="";
		    this.div.innerHTML="";
		    term=0;
        }
		else {
	  		top.status='Assigned trainee '+firstName+' '
	  		  +lastName+' (ID '+traineeID+') to seat.'
	  		this.traineeID=traineeID;
	  		this.traineeFirstName=firstName;
	  		this.traineeLastName=lastName;
	  		this.traineeTerm=term;
	  		this.traineeSendingLocality=sendingLocality;
		
		    this.div.innerHTML = '<b>'+dojo.string.escapeXml(firstName+' '+lastName)+'</b>'+'<br>'+dojo.string.escapeXml(sendingLocality);
            
            refreshList();
        }
        switch (term) {
			case '1':
				this.div.className='secondSeat';
				break;
			case '2':
				this.div.className='thirdSeat';
				break;
			case '3':
				this.div.className='fourthSeat';
				break;
			default:
				this.div.className='seat';
		}
	},

	getTraineeID: function() {
		return this.traineeID || 0;
	},

	update: function() {
		this.x = this.td.cellIndex;
		this.y = this.td.parentNode.rowIndex;
	}
});

/* SeatEditor
****************************/

// PROBLEM: Any trainee who has already been assigned on the current
// seating chart should not have their name in the current drop-down box.


function SeatEditor(node, seatingChart) {
	this.node = dojo.byId(node);
	this.seatingChart = seatingChart;
	this.form = this.node.getElementsByTagName("form")[0];

	var close = this.getItem("close");
	if(close)
		dojo.event.connect(close, "onclick", this, "closeClick");

	dojo.event.connect(this.getItem("clear"), "onclick", this, "onclear");

	dojo.event.connect(this.form, "onsubmit", this, "submit");
}
dojo.lang.extend(SeatEditor, {
	node: null,
	seatingChart: null,
	form: null,
	seat: null,

    	getItem: function(cls, idx) {
		return dojo.html.getElementsByClass(cls, this.node)[idx||0];
	},

	onclear: function(e) {
		e.preventDefault();
		this.seat.setTrainee(0);
		this.clearForm();
		this.onSubmit(this.getTraineeID());
		this.hide(true);
	},

	submit: function(e) {
		e.preventDefault();
		this.onSubmit(this.getTraineeID());
		this.hide(true);
	},

	onSubmit: function(value) {},

	closeClick: function(e) {
		e.preventDefault();
		this.hide(true);
	},

	show: function(seat) {
		this.node.style.display = "block";
		if(seat) {
			var pos = dojo.html.getAbsolutePosition(seat.td);
			dojo.html.placeOnScreen(this.node,
				pos.x + seat.td.offsetHeight/2, pos.y + seat.td.offsetHeight/2, 5);
			this.seat = seat;
		} else {
			this.seat = null;
		}
		// Focus on the input select box.
		var box=this.form.traineeSelect;
		box.focus();
		// Select the trainee, if any.
		var traineeID=this.getTraineeID();
		box.options.selectedIndex=0;
		if(traineeID) {
		    for(var i=box.options.length-1;i>=0;i--) {
		        if(box.options[i].value==traineeID) {
		            box.options.selectedIndex=i;
		            break;
		        }
		    }
		}
	},

	hide: function(andClear) {
		if(andClear) {this.form.reset();}
		this.node.style.display = "none";
		this.seat = null;
		this.onHide();
	},

	onHide: function() {},

	getTraineeID: function() {
		return this.form.traineeID.value;
	},

	getTraineeFirstName: function() {
		return this.form.traineeFirstName.value;
	},

	getTraineeLastName: function() {
		return this.form.traineeLastName.value;
	},
	
	getTraineeTerm: function() {
		return this.form.traineeTerm.value;
	},

    getTraineeSendingLocality: function() {
		return this.form.traineeSendingLocality.value;
	},

	setTraineeID: function(traineeID) {
		this.form.traineeID.value=traineeID;
	},

	clearForm: function() {
		this.form.traineeID.value=0;
		this.form.traineeFirstName.value="";
		this.form.traineeLastName.value="";
	}
});


/* SeatLoader
****************************/

var SeatLoader = {
	url: fttaUrl("attendance/rolldata/seatingChart.ajax.php"),

	chart: function(id) {
		return dojo.byId("seatingChart" + id);
	},

	chartBox: function() {
		return dojo.byId("seating-chart-box");
	},

	formHandler: function(form) {
		var id = form.seatingChart.value;

		if(!isNaN(id)) {
			var chart = SeatLoader.chart(id);

			// 1 check to see if this seating chart is already loaded
			if(chart) {
				SeatLoader.useChart(id);
			} else { // 2 otherwise, go get it!
				SeatLoader.loadChart(id);
			}
		}
	},
	
	loadChart: function(id) {
		dojo.io.bind({
			url: SeatLoader.url,
			method: "get",
			mimetype: "text/json",
			content: { seatingChartID: id },
			handler: SeatLoader.loadHandler(id)
		});
	},

	loadHandler: function(id) {
		return function(type, data, event) {
			if(type == "load") {
				if(data.success) {
					SeatLoader.addChart(id, data.value);
					SeatLoader.useChart(id);
				}
			}
		}
	},

	useChart: function(id) {
		var box = SeatLoader.chartBox();
		var childs = box.childNodes;
		var chart = SeatLoader.chart(id);
		for(var i = 0; i < childs.length; i++) {
			var elm = childs[i];
			if(dojo.html.hasClass(elm, "seating-chart-container")) {
				elm.style.display = elm == chart ? "" : "none";
			}
		}
		dg.hide();
	},

	addChart: function(id, html) {
		var tmp = document.createElement("div");
		tmp.innerHTML = html;
		var box = SeatLoader.chartBox();
		while(tmp.childNodes.length > 0) {
			box.appendChild(tmp.childNodes[0]);
		}

		var chart = SeatLoader.chart(id);
		chart.style.display = "none";
		new SeatingChart(chart).setDataGrid(dg);
	}
}
