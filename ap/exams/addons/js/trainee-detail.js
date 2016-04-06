/* Trainee Report Detail
 *
 *
 * Author: David Schontzler
 * Requirees: dojo.js
 *
 * This adds edit-in-place capabilities to the trainee detail report
**/

function TraineeDetailEditor(node) {
	this.node = dojo.byId(node);
	if(!this.node) { return; }

	var entries = dojo.html.getElementsByClassName("entry", this.node);
	for(var i = 0; i < entries.length; i++) {
		this.addEvents(entries[i]);
	}

	dojo.event.connect(document, "onclick", this, "documentClick");
}

dojo.lang.extend(TraineeDetailEditor, {
	node: null,
	editLink: null,
	editBox: null,
	currentEntry: null,
	formEntry: null, // the entry currently tied to the form
	url: fttaUrl("attendance/rolldata/editCell.php"),
	async: null,

	addEvents: function(entry) {
		dojo.event.connect(entry, "onmouseover", this, "mouseover");
		dojo.event.connect(entry, "onmouseout", this, "mouseout");
	},

	documentClick: function(e) {
		if(this.editBox && !dojo.html.isDescendantOf(e.target, this.editBox)) {
			this.hideEditBox();
		}
	},

	mouseover: function(e) {
		clearTimeout(this.hideTimer);
		this.showEditLink(e.currentTarget);
	},

	mouseout: function(e) {
		this.hideTimer = setTimeout(dojo.lang.hitch(this, function() {
			this.hideEditLink(e.currentTarget);
		}), 20);
	},

	editMouseover: function(e) {
		clearTimeout(this.hideTimer);
	},

	editMouseout: function(e) {
		this.hideTimer = setTimeout(dojo.lang.hitch(this, function() {
			this.hideEditLink(e.currentTarget);
		}), 20);
	},

	editClick: function(e) {
		this.showEditBox(e.clientX, e.clientY);
		e.preventDefault();
		try { e.target.blur(); } catch(E) {}
		e.stopPropagation();
	},

	getEditLink: function() {
		if(!this.editLink) {
			var a = document.createElement("a");
			a.href = "#";
			a.innerHTML = "edit";
			a.id = "trainee-detail-edit-link";
			document.body.appendChild(a);
			dojo.event.connect(a, "onmouseover", this, "editMouseover");
			dojo.event.connect(a, "onmouseout", this, "editMouseout");
			dojo.event.connect(a, "onclick", this, "editClick");
			this.editLink = a;
		}
		return this.editLink;
	},

	showEditLink: function(entry) {
		var lnk = this.getEditLink();
		lnk.style.display = "block";
		var pos = dojo.html.getAbsolutePosition(entry, true);
		lnk.style.left = pos.x + "px";
		lnk.style.top = pos.y + "px";
		this.currentEntry = entry;
	},

	hideEditLink: function() {
		if(this.editLink) {
			this.getEditLink().style.display = "none";
		}
	},

	getEditBox: function() {
		if(!this.editBox) {
			var box = document.createElement("div");
			box.id = "trainee-detail-edit-box";
			box.innerHTML = '<strong id="edit-box-loading">Loading...</strong>'
				+ '<form id="edit-box-form"><strong>Edit value:</strong><br />'
				+ '<input type="text" name="data" size="2" autocomplete="off" />'
				+ '<input type="hidden" name="rollID" />'
				+ '<input type="hidden" name="traineeID" />'
				+ '<input type="submit" value="Save" />'
				+ '</form>'
				+ '<strong id="edit-box-saving">Saving...</strong>';
			document.body.appendChild(box);
			this.editBox = box;
			dojo.event.connect(dojo.byId("edit-box-form"), "onsubmit", this, "formSubmit");
		}
		return this.editBox;
	},

	showEditBox: function(x, y) {
		var box = this.getEditBox();
		box.style.display = "block";
		dojo.html.placeOnScreen(box, x, y);
		this.loadEntry();
	},

	hideEditBox: function() {
		if(this.editBox) {
			this.getEditBox().style.display = "none";
			this.cancelEntry();
			dojo.byId("edit-box-loading").style.display = "block";
			dojo.byId("edit-box-form").style.display = "none";
			dojo.byId("edit-box-saving").style.display = "none";
		}
		this.formEntry = null;
	},

	loadEntry: function() {
		this.cancelEntry();
		dojo.byId("edit-box-loading").style.display = "block";
		dojo.byId("edit-box-form").style.display = "none";
		dojo.byId("edit-box-saving").style.display = "none";

		if(!this.currentEntry) { return; }

		this.formEntry = this.currentEntry;

		var id = this.currentEntry.getAttribute("rollid");
		var trainee = this.currentEntry.getAttribute("traineeid");

		this.cancelEntry();

		this.async = dojo.io.bind({
			url: this.url,
			method: "post",
			mimetype: "text/json",
			content: {
				id: id,
				trainee: trainee,
				action: "getValue"
			},
			handler: dojo.lang.hitch(this, function(type, data, event) {
				if(type == "load") {
					this.populateEntry(id, trainee, data);
				} else {
					this.cancelEntry();
					alert("Couldn't connect to the server. Try again.");
				}
			})
		});
	},

	cancelEntry: function() {
		if(this.async) {
			try { this.async.abort(); } catch(E) {}
		}
	},

	populateEntry: function(id, trainee, data) {
		dojo.byId("edit-box-loading").style.display = "none";
		dojo.byId("edit-box-saving").style.display = "none";

		var form = dojo.byId("edit-box-form");
		form.style.display = "block";
		form.rollID.value = id;
		form.traineeID.value = trainee;
		form.data.value = data.value;
		try {
			form.data.focus();
			form.data.select();
		} catch(E) {}
	},

	formSubmit: function(e) {
		e.preventDefault();
		var form = dojo.byId("edit-box-form");
		dojo.byId("edit-box-loading").style.display = "none";
		dojo.byId("edit-box-saving").style.display = "block";
		form.style.display = "none";

		dojo.io.bind({
			url: this.url,
			method: "post",
			mimetype: "text/json",
			content: {
				id: form.rollID.value,
				trainee: form.traineeID.value,
				value: form.data.value,
				action: "saveValue"
			},
			handler: dojo.lang.hitch(this, function(type, data, event) {
				if(data.action == "remove") {
					dojo.html.addClass(this.formEntry, "removed");
				} else {
					dojo.html.removeClass(this.formEntry, "removed");
				}
				this.hideEditBox();
				if(data.message) {
					alert(data.message);
				}
			})
		});
	}
});
