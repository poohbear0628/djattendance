/* ComboBox
 *
 * Author: David Schontzler
 * Requires: dojo.js, combo-box.css
 *
 * This is more of a typing-select box at the moment that can be used for things like
 * trainee names and the like. It replaces a <select> box. If needed, we can make this
 * behave as a general-purpose combo box where you can either a) use existing values or
 * b) submit new ones.
**/
function ComboBox(node, args /* onlyExistingValues, resultsOnTop */) {
	this.node = dojo.byId(node); // <select> box
	if(!this.node) { return; }
	if(!args) { args = {}; }
	if(args.onlyExistingValues) {
		args["acceptNewValues"] = false;
	}
	try {
		dojo.lang.mixin(this, args);
	} catch(E) {} // IE freaks out sometimes
	this.values = [];

        var classes = this.node.className;
        var styles = this.node.style.cssText;
        var newName = this.node.name+'_autocomplete';
        newName = newName.replace(/[_\[\]]+/g, "_");
	if(this.node.multiple) {
		this.multipleValue = true;
		this.input = dojo.html.createNodesFromText('<textarea '
			+ 'id="' + newName + '" '
			/*+ 'name="' + this.node.name.replace(/[\[\]]+/g, "_") + '_autocomplete" '*/ //I removed this because it isn't really necessary and it clutters the URL ba
			+ 'class="combo-box-textarea '+classes+'" style="height:6em;'+styles+'"></textarea>', true)[0];
        } else {
		this.input = dojo.html.createNodesFromText('<input type="text" autocomplete="off" '
			+ 'id="' + newName + '" '
			/*+ 'name="' + this.node.name.replace("[]", "") + '_autocomplete" '*/ //I removed this because it isn't really necessary and it clutters the URL ba
			+ 'class="combo-box-input '+classes+'" style="'+styles+'" />', true)[0];
	}
	dojo.event.connect(this.input, "onfocus", this, "focus");
	dojo.event.connect(this.input, "onkeydown", this, "keydown");
	dojo.event.connect(this.input, "onkeyup", this, "keyup");
	dojo.event.connect(this.input, "ondblclick", this, "dblclick");
	dojo.event.connect(this.input, "onblur", this, "blur");
	dojo.html.insertBefore(this.input, this.node);
	if(this.node.form) {
		dojo.event.connect(this.node.form, "onsubmit", this, "submit");
	}

	if(!this.multipleValue) {
		this.valueInput = dojo.html.createNodesFromText('<input type="hidden" '
			+ 'id="' + this.node.name + '" '
			+ 'name="' + this.node.name + '" />', true)[0];
		dojo.html.insertBefore(this.valueInput, this.node);
	}

	// so we only get one form element with the given name, we must remove the <select>
	this.node.parentNode.removeChild(this.node);

	this.box = dojo.html.createNodesFromText('<div class="combo-box" style="max-height:' +
            (this.maxResultsVisible * 1.54) + 'em"></div>', true)[0];
	dojo.event.connect(this.box, "onmouseover", this, "mouseover");
	dojo.body().appendChild(this.box);

	dojo.event.connect(document, "onclick", this, "onclick");

	this.node.style.display = "none";

	this.populate(this.node);

	// take care of pre-selected value
	var sel = this.node.selectedIndex;
	if(sel >= 0) {
		if(this.multipleValue) {
			var ops = this.node.options;
			var vals = [];
			for(var i = 0; i < ops.length; i++) {
				if(ops[i].selected) {
					vals.push(ops[i].text);
				}
			}
			this.input.value = vals.join(", ");
			this.updateValue();
		} else {
			var selected = this.node.options[sel];
			this.setValue(selected.text);
		}
	}

	// look for instructions
	if(dojo.html.getAttribute(this.node, "selectOnFocus") == 1) {
		this.selectOnFocus = true;
	}

	if(dojo.html.getAttribute(this.node, "clearOnFocus") == 1) {
		this.clearOnFocus = true;
	}

	// connect any events
	if(dojo.html.getAttribute(this.node, "onSelectOption")) {
		var fcn = new Function("e", dojo.html.getAttribute(this.node, "onSelectOption"));
		dojo.event.connect(this, "onSelectOption", dojo.lang.hitch(this.input, fcn));
	} else if(dojo.html.getAttribute(this.node, "onchange")) {
		var fcn = new Function("e", dojo.html.getAttribute(this.node, "onchange"));
		dojo.event.connect(this, "onSelectOption", dojo.lang.hitch(this.input, fcn));
	}

	if(dojo.html.getAttribute(this.node, "onConfirmSelection")) {
		var fcn = new Function("e", dojo.html.getAttribute(this.node, "onConfirmSelection"));
		dojo.event.connect(this, "onConfirmSelection", dojo.lang.hitch(this.input, fcn));
	}

	// other attributes we might want
	if(dojo.html.getAttribute(this.node, "tabindex")) {
		this.input.setAttribute("tabindex", dojo.html.getAttribute(this.node, "tabindex"));
	}

	if(dojo.html.getAttribute(this.node, "accesskey")) {
		this.input.setAttribute("accesskey", dojo.html.getAttribute(this.node, "accesskey"));
	}
}
dojo.lang.extend(ComboBox, {
	node: null,
	box: null,
	input: null,
	multipleValue: false, // gmail style
	blankValue: null, // what to use for blank value
	valueInput: null, // store the value here
	values: null, // for multipleValue
	maxResultsVisible: 9, // max search results above the scroll
	maxResults: Infinity, // max search results
	resultsOnTop: false, // show results above input

	selectOnFocus: true,
	clearOnFocus: false,

	// if selected by pressing Enter we need to know to prevent form submittal
	enterSelect: false,

	clearInvalidValues: true,
	acceptNewValues: true,
	existingValue: false,
	messages: {
		notExistingValue: "That name doesn't exist!"
	},

	populate: function(sel) {
		this.data = {};

		if(dojo.html.isTag(sel, "select")) {
			var opts = sel.options;
			for(var i = 0; i < opts.length; i++) {
				if(!opts[i].text) {
					// take the first blank option w/a value as the default blank value
					if(opts[i].value && this.blankValue == null) {
						this.blankValue = opts[i].value;
					}
					continue;
				}
				//if(!opts[i].text || !opts[i].value) { continue; }
				this.data[opts[i].text] = {
					key: opts[i].text,
					value: opts[i].value,
					description: opts[i].title
				};
			}
		} else {
			dojo.lang.mixin(this.data, sel);
		}
	},

	onclick: function(e) {
		var node = e.target;
		if(dojo.html.isDescendantOf(node, this.box)) {
			this.selectResult();
			this.autoFocus = true;
			this.input.focus();
		}
		if(!dojo.html.isDescendantOf(node, this.input)) {
			this.hideResults();
		}
	},

	tabComplete: function() {
		if(this.resultsVisible() && this.highlightedItem) {
			this.selectResult();
			setTimeout(dojo.lang.hitch(this, function(){
				this.autoFocus = true;
				this.input.focus();
			}), 0);
		}
		this.hideResults();
	},

	focus: function(e) {
		if(!this.autoFocus) {
			if(this.clearOnFocus) {
				this.input.value = "";
			} else if(!this.multipleValue && this.selectOnFocus) {
                            this.input.select();
                            //added by Allen Webb to fix a weird glitch in google chrome
                            param = this.input;
                            setTimeout(function(){if(param)param.select();param=null;},250);
                            //end of addition
			}
		}
		this.autoFocus = false;
		this.enterSelect = false;
		this.startSearch(this.input.value, true);
	},

	submit: function(e) {
		this.updateValue();

		if(!this.multipleValue && this.enterSelect) {
			e.preventDefault();
		} else if(!this.acceptNewValues && !this.existingValue) {
			alert(this.messages.notExistingValue);
			e.preventDefault();
		}
		this.enterSelect = false;
	},

	keydown: function(e) {
		switch(e.keyCode) {
			case e.KEY_UP_ARROW:
				if(this.highlightPreviousItem()) {
					e.preventDefault();
				}
				break;
			case e.KEY_DOWN_ARROW:
				if(this.highlightNextItem()) {
					e.preventDefault();
				} else if(!this.resultsVisible()){
					this.showAll();
				}
				break;
			case 188: // comma:
				if(this.multipleValue) {
					e.preventDefault();
				} else {
					break;
				}
			case e.KEY_TAB:
				this.tabComplete();
				break;
			case e.KEY_ENTER:
				if(this.resultsVisible()) {
					this.enterSelect = true;
				}
				break;
		}
	},

	lastValue: "",

	keyup: function(e) {
		if(e.ctrlKey) {
                    var code;
                    if (!e) var e = window.event;
                    if (e.keyCode) code = e.keyCode;
                    else if (e.which) code = e.which;
                    if(code==86){
                        var failed_values = this.updateValue();
                        if(this.multipleValue && failed_values)
                            if(failed_values.length) alert("The following input was not recognized: "+failed_values.join(", "));
                            else alert("The input you entered was all recognized!");
                    }
                    return;
                }
		switch(e.keyCode) {
			case e.KEY_ESCAPE:
				this.hideResults();
				break;
			case e.KEY_ENTER:
				this.selectResult();
				break;
			case e.KEY_TAB:
				this.hideResults();
				break;
			case e.KEY_HOME:
			case e.KEY_END:
			case e.KEY_SHIFT:
			case e.KEY_LEFT_ARROW:
			case e.KEY_RIGHT_ARROW:
				break;
			default:
				var value = this.input.value;
				if(this.multipleValue && value) {
					var parts = value.split(/\s*,\s*/);
					value = parts[parts.length-1];
				}

				if(value != this.lastValue) {
					this.onChange(value, this.lastValue);
					this.lastValue = value;
					this.startSearch(value);
				}
		}
	},

	mouseover: function(e) {
		var node = e.target;
		while(node && node != this.box) {
			if(dojo.html.hasClass(node, "combo-box-item")) {
				this.highlightItem(node);
				break;
			}
			node = node.parentNode;
		}
	},

	dblclick: function(e) {
		if(!this.multipleValue && this.input.value == "") {
			this.showAll();
		}
	},

	blur: function(e) {
		if(!this.multipleValue) {
			if(!this.resultsVisible()) {
				this.setValue(this.input.value);
			}
		}
	},

	onChange: function(newValue, oldValue) {
	},

	showResults: function() {
                this.box.style.width = this.input.offsetWidth;
		var pos = dojo.html.getAbsolutePosition(this.input, true);
		this.box.style.left = pos.x + "px";
		if(this.resultsOnTop) {
			this.box.style.bottom = (dojo.html.getDocumentHeight() - pos.y + 2) + "px";
			this.box.style.top = "";
		} else {
			this.box.style.bottom = "";
			this.box.style.top = pos.y + this.input.offsetHeight + "px";
		}
		this.highlightNextItem();
		this.box.style.display = "block";
		this.box.scrollTop = 0;
	},

	hideResults: function() {
		this.box.style.display = "none";
	},

	resultsVisible: function() {
		return this.box.style.display == "block";
	},

	selectResult: function() {
		if(this.highlightedItem) {
			var value = this.highlightedItem.getAttribute("key");
			this.hideResults();
			this.setValue(value);
			this.generateEvent("onSelectOption", value);
		} else if(!this.resultsVisible()) {
			this.setValue(this.input.value);
			this.generateEvent("onConfirmSelection", this.input.value);
		}
	},

	onSelectOption: function(value) {},
	onConfirmSelection: function(value) {},
	onInvalidValue: function(value) {
		if(this.clearInvalidValues && !this.acceptNewValues) {
			this.setValue("");
			this.generateEvent("onSelectOption", this.blankValue);
			return true;
		}
		return false;
	},

	generateEvent: function(evt, text) {
		if(this[evt]) {
			this[evt]({
				event: evt,
				text: text,
				value: this.valueInput.value
			});
		}
	},

	highlightedItem: null,

	highlightNextItem: function() {
		var node = this.highlightedItem;
		if(node) {
			node = dojo.html.nextElement(node);
		}
		// either at beginning or end of list
		if(!node) {
			node = dojo.html.firstElement(this.box);
		}

		this.highlightItem(node);
		this.keepNodeInView(node);
		return this.resultsVisible();
	},

	highlightPreviousItem: function() {
		var node = this.highlightedItem;
		if(node) {
			node = dojo.html.prevElement(node);
		}
		// either at beginning or end of list
		if(!node) {
			node = dojo.html.lastElement(this.box);
		}

		this.highlightItem(node);
		this.keepNodeInView(node);
		return this.resultsVisible();
	},

	highlightItem: function(node) {
		if(this.highlightedItem) {
			dojo.html.removeClass(this.highlightedItem, "highlighted");
		}
		if(node) {
			dojo.html.addClass(node, "highlighted");
		}
		this.highlightedItem = node;
	},

	keepNodeInView: function(node) {
		if(node) {
			var boxTop = this.box.scrollTop;
			var boxBottom = boxTop + this.box.offsetHeight;
			var top = node.offsetTop;
			var bottom = top + node.offsetHeight;

			if(top < boxTop) {
				this.box.scrollTop = Math.max(0, top);
			} else if(bottom > boxBottom) {
				this.box.scrollTop += (bottom - boxBottom) + 3;
			}
		}
	},

	showAll: function() {
		var items = [];
		for(var key in this.data) {
			items.push(this.data[key]);
		}

		items.sort(function(A, B) {
			var a = A.key, b = B.key;
			if(a > b) { return 1; }
			if(a < b) { return -1; }
			return 0;
		});

		this.provideResults(items, null);
	},

	startSearch: function(value, needsMultiple) {
		value = value.replace(/^\W+/, "");
		var items = [];
		var reString = "(\\s|^)(" + dojo.string.escapeRegExp(value) + ")";
		var re = new RegExp(reString, "ig");
		if(value) {
			for(var key in this.data) {
				// dup it here, otherwise test() doesn't work properly, not sure why
				re = new RegExp(reString, "ig");
				if(re.test(key)) {
					items.push(this.data[key]);
				}
				if(items.length >= this.maxResults) {
					break;
				}
			}
			items.sort(function(a, b) {
				return a.key > b.key;
			});
		}

		if(needsMultiple && items.length < 2) { return; }
		this.provideResults(items, re);
	},

	provideResults: function(items, re) {
		this.updateValue();
		this.clearResults();
		if(items.length > 0) {
			for(var i = 0; i < items.length; i++) {
				var item = items[i];
				var node = document.createElement("div");
				node.setAttribute("key", item.key);
				node.setAttribute("value", item.value);
				node.setAttribute("title", item.description);
				node.className = "combo-box-item";
				var str = item.key;
				if(re) {
					str = str.replace(re, "<strong>$1$2</strong>");
				}
				node.innerHTML = str;
				this.box.appendChild(node);
			}
			this.showResults();
		} else {
			this.hideResults();
		}
	},

	clearResults: function() {
		dojo.html.removeChildren(this.box);
	},

	setValue: function(value) {
		if(this.multipleValue) {
			var parts = this.input.value.split(/,([^,]+)$/);
			if(this.input.value == parts[0]) {
				this.input.value = value;
			} else {
				this.input.value = parts[0] + ", " + value;
			}
			this.input.value += ", ";
		} else {
			var stopProcessing = false;
			if(value && !this.acceptNewValues && !this.data[value]) {
				stopProcessing = this.onInvalidValue(value);
			}
			if(stopProcessing) { return; }
			this.input.value = value;
		}
		this.updateValue();
	},

	getValue: function() {
	},

	updateValue: function() {
		var value = this.input.value;
		if(this.multipleValue) {
			// clear current values
			for(var i = 0; i < this.values.length; i++) {
				dojo.html.removeNode(this.values[i]);
			}
			this.values = [];

			var addValue = dojo.lang.hitch(this, function(name, value) {
				var input = dojo.html.createNodesFromText('<input type="hidden" name="'
					+ name + '" value="' + value + '" />', true)[0];
				dojo.html.insertBefore(input, this.input);
				this.values.push(input);
				this.valueInput = input;
				return input;
			});

			// create new values
			var parts = value.split(/\s*,\s*/);
			this.existingValue = true;
                        var new_values = [];
			for(var i = 0; i < parts.length; i++) {
				var val = parts[i];
				if(!val) { continue; }
				var accept = true;
				if(this.data[val]) {
					val = this.data[val].value;
				} else {
                                        new_values.push(val);
					this.existingValue = false;
					if(!this.acceptNewValues) {
						accept = false;
					}
				}

				if(accept) {
					var input = addValue(this.node.name, val);
				}
			}

			// fill in the blank value
			if(!this.values.length && this.blankValue != null) {
				var input = addValue(this.node.name, this.blankValue);
			}
                        return new_values;
		} else {
			if(this.data[value]) {
				this.valueInput.value = this.data[value].value;
				this.existingValue = true;
			} else if(dojo.string.trim(value) == "" && this.blankValue != null) {
				this.valueInput.value = this.blankValue;
				this.existingValue = true;
				this.generateEvent("onSelectOption", this.blankValue);
			} else {
				this.valueInput.value = "";
				this.existingValue = false;
			}
		}
	}
});

dojo.lang.mixin(ComboBox, {
	_pageLoaded: false,
	_waitingToInit: [],

	add: function(node, args, selectBox) {
		this._waitingToInit.push(function() {
			if(selectBox) {
				new SelectBox(node, args);
			} else {
				new ComboBox(node, args);
			}
		});
		ComboBox._doInit();
	},

	_doInit: function() {
		if(ComboBox._pageLoaded) {
			var cb = ComboBox._waitingToInit;
			while(cb.length) {
				cb.shift()();
			}
		}
	}
});

dojo.addOnLoad(function() {
	ComboBox._pageLoaded = true;
	ComboBox._doInit();
});

function SelectBox(node, args) {
	ComboBox.call(this, node, args);
}
dojo.inherits(SelectBox, ComboBox);

SelectBox.add = function(node, args) {
	if(!args) { args = {}; }
	args.onlyExistingValues = true;
	ComboBox.add(node, args, true);
}