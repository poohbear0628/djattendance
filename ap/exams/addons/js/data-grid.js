/* DataGrid
 *
 * Author: David Schontzler
 *
 * Here's where functionality for grids of inputs (i.e. roll data) should live.
 *
 * Example usage (where table has ID of "grid"):
 *  dojo.addOnLoad(function() { new DataGrid("grid"); });
**/

function DataGrid(table, args) {
	args = dojo.lang.mixin(this._args, args);

	this.table = dojo.byId(table);
	this.init();

	if(!args.highlightRows) {
		this.disableHighlightRows();
	}

	if(!args.stickyHeader) {
		this.disableStickyHeader();
	}

	if(args.mode == DataGrid._modes.FLOATING) {
		this.setMode(DataGrid._modes.FLOATING);
	}
}
DataGrid._modes = {
	DEFAULT: "default",
	FLOATING: "floating"
}
DataGrid.prototype = {
	table: null,
	tableX : null,
	enabled: false,
	_highlightRows: true,
	_stickyHeader: true,
	_mode: DataGrid._modes.DEFAULT,
	_args: {
		highlightRows: true,
		stickyHeader: true
	},

	init: function() {
		if(!this.table) { return; }
		var boxes = this.table.getElementsByTagName("input");
		var n = 0;
		for(var i = 0; i < boxes.length; i++) {
			var box = boxes[i];
			if(box.type == "text") {
				dojo.event.connect(box, "onkeydown", this, "_keydown");
				dojo.event.connect(box, "onfocus", this, "_focus");
				n++;
			}
		}
		this.enable();
		this.initStickyHeader();
	},

	enable: function() {
		this.enabled = true;
	},

	disable: function() {
		this.enabled = false;
	},

	show: function() {
		this.table.style.display = "";
	},

	hide: function() {
		this.table.style.display = "none";
	},

	enableHighlightRows: function() {
		if(!this._highlightRows) {
			this._highlightRows = true;
		}
	},

	disableHighlightRows: function() {
		if(this._highlightRows) {
			this._highlightRows = false;
			if(this._currentRow) {
				dojo.html.removeClass(this._currentRow, "current");
			}
		}
	},

	enableStickyHeader: function() {
		this._stickyHeader = true;
		this.scroll();
	},

	disableStickyHeader: function() {
		this._stickyHeader = false;
		this.hideClonedHeader();
	},

	floatingSubmit: function(e) {
		if(this.form) {
			this.setMode();
		}
	},

	setMode: function(mode) {
		var M = DataGrid._modes;
		if(!mode) { mode = M.DEFAULT; }

		switch(mode) {
			case M.FLOATING:
				this._mode = M.FLOATING;
//				this.disableHighlightRows();
//				this.disableStickyHeader();
//				this.hide();
//				dojo.html.addClass(this.table, "floating");
//				this._placeHolder = document.createElement('span');
//				this.table.parentNode.insertBefore(this._placeHolder, this.table);
				var form = dojo.html.getParentByType(this.table, "form");
				if(form) {
					this.form = form;
					dojo.event.connect(form, "onsubmit", this, "floatingSubmit");
				}
				//document.body.appendChild(this.table);
				break;
			default:
				this.enableHighlightRows();
				this.enableStickyHeader();
				this.filterRow();
				dojo.html.removeClass(this.table, "floating");
				if(this._placeHolder) {
					this._placeHolder.parentNode.insertBefore(this.table, this._placeHolder);
					this._placeHolder.parentNode.removeChild(this._placeHolder);
					delete this._placeHolder;
				}
				if(this.form) {
					this.form = null;
				}
				this.show();
				this._mode = M.DEFAULT;
		}

		return this._mode;
	},

	filterRow: function(id) {
		var found = null;
		if(this._mode == DataGrid._modes.FLOATING) {
			var rows = this.table.tBodies[0].rows;
			for(var i = 0; i < rows.length; i++) {
				var row = rows[i];
				if(!id || row.id == id) {
					row.style.display = "";
					dojo.html.removeClass(row, "shadeRow");
					found = row;
				} else {
					row.style.display = "none";
				}
			}
			this.show();
		} else {
			// just try and jump to that row
			location = "#" + id;
		}
		return found;
	},

	showAllRows: function() {
                var rows = this.table.tBodies[0].rows;
                for(var i = 0; i < rows.length; i++) {
                        rows[i].style.display = "";
                }
		dojo.html.removeClass(this.table, "floating");
                this.show();
	},

	placeTable: function(x, y) {
		if(this._mode == DataGrid._modes.FLOATING) {
			dojo.html.placeOnScreen(this.table, x, y, 5, true);
			this.show();
		}
	},

	filterAndPlace: function(id, x, y) {
		var row = this.filterRow(id);
		if(row) {
			this.placeTable(x, y);
			try {
				var ins = row.getElementsByTagName("input")
				for(var i = 0; i < ins.length; i++) {
					if(ins[i].type == "text") {
						ins[i].focus();
						break;
					}
				}
			} catch(E) {};
		} else {
			this.hide();
		}
	},

	_keydown: function(e) {
		if(this.enabled) {
			if(!e.ctrlKey && !e.shiftKey && !e.altKey) {
				var box = e.currentTarget;
				switch(e.keyCode) {
					case e.KEY_UP_ARROW:
						this.moveUp(box);
						break;
					case e.KEY_DOWN_ARROW:
						this.moveDown(box);
						break;
					case e.KEY_LEFT_ARROW:
						this.moveLeft(box);
						break;
					case e.KEY_RIGHT_ARROW:
						this.moveRight(box);
						break;
					case e.KEY_PAGE_UP:
						this.pageUp(box);
						break;
					case e.KEY_PAGE_DOWN:
						this.pageDown(box);
						break;
				}
			}
		}
	},

	_focus: function(e) {
		if(this.enabled && this._highlightRows) {
			var box = e.currentTarget;
			var row = this.cell(box).parentNode;
			if(this._currentRow && this._currentRow != row) {
				dojo.html.removeClass(this._currentRow, "current");
			}
			this._currentRow = row;
			dojo.html.addClass(this._currentRow, "current");
		}
	},

	cell: function(box) {
		return box.parentNode;
	},

	pickBox: function(box, dir) {
		try {
			// if the height is 0 then it isn't visible
			if(box && box.offsetHeight > 0) {
				box.focus();
			}
		} catch(e) {}
	},

	moveUp: function(box) {
		var c = this.cell(box);
		var tr = c.parentNode;
		var prevTr = dojo.html.prevElement(tr);
		if(prevTr) {
			var td = prevTr.cells[c.cellIndex];
			var newBox = td.getElementsByTagName("input")[0];
			if(newBox && newBox.type == "text") {
				this.pickBox(newBox);
			}
		}
	},

	moveDown: function(box) {
		var c = this.cell(box);
		var tr = c.parentNode;
		var nextTr = dojo.html.nextElement(tr);
		if(nextTr) {
			var td = nextTr.cells[c.cellIndex];
			var newBox = td.getElementsByTagName("input")[0];
			if(newBox && newBox.type == "text") {
				this.pickBox(newBox);
			}
		}
	},

	moveLeft: function(box) {
		if(this.selectionAtStart(box)) {
			var c = this.cell(box);
			var td = dojo.html.prevElement(c);
			if(td) {
				var newBox = td.getElementsByTagName("input")[0];
				if(newBox && newBox.type == "text") {
					this.pickBox(newBox, "left");
				}
			}
		}
	},

	moveRight: function(box) {
		if(this.selectionAtEnd(box)) {
			var c = this.cell(box);
			var td = dojo.html.nextElement(c);
			if(td) {
				var newBox = td.getElementsByTagName("input")[0];
				if(newBox && newBox.type == "text") {
					this.pickBox(newBox, "right");
				}
			}
		}
	},

	pageCells: 25, // how many cells to jump w/page-up/down

	pageUp: function(box) {
		var c = this.cell(box);
		var tr = c.parentNode;
		var count = 0;
		while(tr && ++count < this.pageCells) {
			var newTr = dojo.html.prevElement(tr);
			if(newTr) {
				tr = newTr;
			} else {
				break;
			}
		}

		if(tr) {
			var td = tr.cells[c.cellIndex];
			var newBox = td.getElementsByTagName("input")[0];
			if(newBox && newBox.type == "text") {
				this.pickBox(newBox);
			}
		}
	},

	pageDown: function(box) {
		var c = this.cell(box);
		var tr = c.parentNode;
		var count = 0;
		while(tr && ++count < this.pageCells) {
			var newTr = dojo.html.nextElement(tr);
			if(newTr) {
				tr = newTr;
			} else {
				break;
			}
		}

		if(tr) {
			var td = tr.cells[c.cellIndex];
			var newBox = td.getElementsByTagName("input")[0];
			if(newBox && newBox.type == "text") {
				this.pickBox(newBox);
			}
		}
	},

	selectionAtStart: function(box) { return this.selectionAt(box, true); },
	selectionAtEnd: function(box) { return this.selectionAt(box, false); },

	selectionAt: function(box, start) {
		if(start) { // is at start?
			if(typeof box.selectionStart != "undefined") {
				return box.selectionStart == 0 && box.selectionEnd == 0;
			} else if(box.createTextRange) {
				return this.getCursorPosition(box) == 0;
			}
		} else { // is at end?
			if(typeof box.selectionStart != "undefined") {
				return box.selectionStart == box.value.length && box.selectionEnd == box.value.length;
			} else if(box.createTextRange) {
				return this.getCursorPosition(box) == box.value.length;
			}
		}
	},

	getCursorPosition: function(node) {
		var cursorPos = -1;
		if(document.selection && document.selection.createRange) {
			var range = document.selection.createRange().duplicate();
			if (range.parentElement() == node) {
				range.moveStart('textedit', -1);
				cursorPos = range.text.length;
			}
		} else if (node.selectionEnd) {
			cursorPos = node.selectionEnd;
		}
		return cursorPos;
	},

	initStickyHeader: function() {
		this.header = this.table.tHead;
		if(this.header) {
			this.headerY = dojo.html.getAbsoluteY(this.header);
			this.tableBottom = dojo.html.getAbsoluteY(this.table) + this.table.offsetHeight;
			dojo.event.connect(window, "onscroll", this, "scroll");
		}
	},

	headerClone: null,

	getClonedHeader: function() {
		function getW(node) {
			return dojo.render.html.ie ? node.offsetWidth + "px" : dojo.style.getComputedStyle(node, "width");
		}

		function getH(node) {
			return dojo.render.html.ie ? node.offsetHeight + "px" : dojo.style.getComputedStyle(node, "height");
		}

		if(!this.headerClone) {
			var wrapper = document.createElement("div");
			wrapper.style.position = "absolute";
			wrapper.style.width = this.table.offsetWidth + "px";

			var tbl = document.createElement("table");
			tbl.className = this.table.className;
			var head = this.header.cloneNode(true);

			var th = this.header.getElementsByTagName("th");
			var newTh = head.getElementsByTagName("th");

			for(var i = 0; i < th.length; i++) {
				newTh[i].style.width = getW(th[i]);
				newTh[i].style.height = getH(th[i]);
			}

			tbl.appendChild(head);
			tbl.style.width = this.table.offsetWidth + "px";
			wrapper.appendChild(tbl);
			document.body.appendChild(wrapper);
			this.headerClone = wrapper;
		}
		return this.headerClone;
	},

	showClonedHeader: function(x, y) {
		var clone = this.getClonedHeader();
		clone.style.left = x + "px";
		clone.style.top = y + "px";
		clone.style.display = "block";
	},

	hideClonedHeader: function() {
		if(this.headerClone) {
			this.headerClone.style.display = "none";
		}
	},

	scroll: function(e) {
		if(this._stickyHeader) {
			var y = dojo.html.getScrollTop();
			if(y > this.headerY && y < this.tableBottom) {
			  if (this.tableX == null) {
				  this.tableX = dojo.html.getAbsoluteX(this.table);
				}
				this.showClonedHeader(this.tableX, y);
			} else {
				this.hideClonedHeader();
			}
		}
	}
};
