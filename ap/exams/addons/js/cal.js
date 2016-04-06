/* Calendar
 *
 * Author: David Schontzler
 *
 * Calendar for viewing your current schedule and/or selecting rolls for leave slips
**/

function Calendar(node) {
	this.node = dojo.byId(node);
	
	if(dojo.html.hasAttribute(this.node, "calendar")) {
        return;
    } else {
        this.node.setAttribute("calendar", "calendar");
    }

	if(dojo.html.hasClass(this.node, "selectable")) {
		this.setSelectable(true);
	}

	dojo.event.connect(this.node, "onclick", this, "onclick");
}

dojo.lang.extend(Calendar, {
	node: null,
	selectable: false,
	
	setSelectable: function(on) {
		this.selectable = Boolean(on);
		if(this.selectable) {
			dojo.html.addClass(this.node, "selectable");
		} else {
			dojo.html.removeClass(this.node, "selectable");
		}
	},

    isSelectable: function()  {
        return this.selectable;
    },

	onclick: function(e) {
		this.toggleSelected(e.target);
	},

	isSelected: function(node) {
		return dojo.html.hasClass(node, "selected");
	},
	
	isEntryBox: function(node) {
		return dojo.html.isTag(node, "div") && dojo.html.hasClass(node, "entry");
	},

	toggleSelected: function(node) {
		if(!this.selectable) { return; }

		if(!this.isEntryBox(node)) {
			return;
		}

		if(this.isSelected(node)) {
			this.deselect(node);
		} else {
			this.select(node);
		}
	},

	getCheckbox: function(node) {
		return node.getElementsByTagName("input")[0];
	},

	select: function(node) {
		dojo.html.addClass(node, "selected");
		var cb = this.getCheckbox(node);
		if(cb) {
			cb.checked = true;
		}
	},

	deselect: function(node) {
		dojo.html.removeClass(node, "selected");
		var cb = this.getCheckbox(node);
		if(cb) {
			cb.checked = false;
		}
	},
	
	setSelectedByCheckbox: function(cb, selected) {	
		var node = cb;
		while(node) {
			if(this.isEntryBox(node)) {
				if(selected) {
					this.select(node);
				} else {
					this.deselect(node);
				}
			}
			node = node.parentNode;
		}
	}
});

