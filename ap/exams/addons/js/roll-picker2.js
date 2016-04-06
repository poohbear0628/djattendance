var PeriodSelector = {
	formName: "pickRollsForm",
	url: fttaUrl("/attendance/rolldata/pickRoll.ajax.php"),
	_currentPeriod: -1,

	init: function() {
		var periods = dojo.byId("periods");
		var a = periods.getElementsByTagName("a");
		for(var i = 0; i < a.length; i++) {
			dojo.event.connect(a[i], "onclick", this, "click");
			if(dojo.html.hasClass(a[i], "active")) {
				this._select(a[i]);
				this._currentPeriod = i;
			}
		}
	},

	click: function(e) {
		e.preventDefault();
		this._select(e.currentTarget);
	},

	_updateForm: function(periodID) {
		var form = document.forms[this.formName];
		if(form) {
			form["selected-period"].value = periodID;
		}
	},

	_showPeriod: function(period) {
		this._hideLoading();
		if(period != this._currentPeriod) {
			this._hidePeriod(this._currentPeriod);
			try{dojo.byId("period"+period).style.display="block"}catch(e){}
			dojo.html.addClass(dojo.byId("period-tab"+period), "active");
			this._currentPeriod = period;
			dojo.byId("period-container").scrollTop = 0;
		}
	},
	
	_hidePeriod: function(period) {
		try{dojo.byId("period"+period).style.display="none"}catch(e){}
		dojo.html.removeClass(dojo.byId("period-tab"+period), "active");
	},

	_showLoading: function() {
		dojo.byId("loading-period").style.display = "block";
		this._hidePeriod(this._currentPeriod);
	},

	_hideLoading: function() {
		dojo.byId("loading-period").style.display = "none";
	},

	_select: function(node) {
		var period = node.getAttribute("period");
		var pid = node.getAttribute("pid");
		this.select(period, pid);
	},

	select: function(period, pid) {
		if(period < 0) { return; }

		if(dojo.byId("period" + period)) {
			this._showPeriod(period);
		} else {
			this._showLoading();
			dojo.io.bind({
				url: this.url,
				content: { periodID: pid, period: period },
				mimetype: "text/json",
				load: dojo.lang.hitch(this, "_load")
			});
		}
		this._updateForm(pid);
	},

	_load : function(type, response, x) {
		if(response.success) {
			var html = response.value;
			var box = dojo.html.createNodesFromText(html, true)[0];
			var pc = dojo.byId("period-container");
			pc.appendChild(box);
			this._showPeriod(response.period);
		}
	}
};

dojo.addOnLoad(function() { PeriodSelector.init(); });

// -------------------------

var AutoCheck = {
	formName: "pickRollsForm",

	_getDisplayId: function(input) {
		return (input.id||("-none-"+new Date().getMilliseconds())) + "-item";
	},

	_getDisplayItem: function(input, create) {
		function pad(x) { x = String(x); return x.length > 1 ? x : "0" + x; }

		var id = AutoCheck._getDisplayId(input);
		var item = dojo.byId(id);
		if(!item && create) {
			var title = input.getAttribute("title");
			var d = new Date(input.getAttribute("date"));
			var displayTxt = " " + title + " (" + (d.getMonth()+1) + "/" + d.getDate() + " @ "
				+ (d.getHours() % 12) + ":" + pad(d.getMinutes()) + (d.getHours() > 11 ? "pm" : "am") + ")";

			var a = document.createElement("a");
			a.innerHTML = "x";
			a.href = "javascript:AutoCheck.removeItem('" + id + "')";
			a.className = "remove";

			var txt = document.createTextNode(displayTxt);

			item = document.createElement("li");
			item.setAttribute("inputid", input.id);
			item.id = id;
			item.appendChild(a);
			item.appendChild(txt);
		}
		return item;
	},

	_rollsSelectedCount: function() {
		var lis = dojo.byId("selected-rolls").getElementsByTagName("li");
		return lis.length - 1;
	},

	_updateDisplay: function(input) {
		if(input.checked) {
			AutoCheck._showDisplayItem(input);
		} else {
			AutoCheck._hideDisplayItem(input);
		}

		var cnt = AutoCheck._rollsSelectedCount();
		var ul = dojo.byId("selected-rolls");
		if(cnt > 0) {
			dojo.html.addClass(ul, "has-items");
		} else {
			dojo.html.removeClass(ul, "has-items");
		}

		dojo.byId("selected-rolls-count").innerHTML = cnt > 0 ? " (" + cnt + ")" : "";
	},

	_showDisplayItem: function(id) {
		var input = dojo.byId(id);
		var item = AutoCheck._getDisplayItem(input, true);
		if(!item.parentNode) {
			dojo.byId("selected-rolls").appendChild(item);
		}
	},

	_hideDisplayItem: function(id) {
		var input = dojo.byId(id);
		var item = AutoCheck._getDisplayItem(input)
		if(item) {
			item.parentNode.removeChild(item);
			delete item;
		}
	},

	_getPeriodGroup: function(id) {
		var input = dojo.byId(id);
		// TODO: implement this
		return {
			period: 0,
			group: 0
		};
	},

	exec: function(periodID, groupID, checked) {
		var inputs = dojo.html.getElementsByClass("autocheckgroup_" + periodID + "_" + groupID);
		for(var i = 0; i < inputs.length; i++) {
			var input = inputs[i];
			if(input.checked != checked) {
				input.checked = checked;
				AutoCheck.click(input);
			}
		}
	},

	click: function(id) {
		var input = dojo.byId(id);
		AutoCheck._updateDisplay(input);

		if(!input.checked) { // TODO: toggle group checkbox accordingly
			var info = AutoCheck._getPeriodGroup(input);
			var cb = dojo.byId("autocheck-" + info.period + "-" + info.group);
			if(cb) {
				cb.checked = false;
			}
		}
	},

	removeItem: function(id) {
		var li = dojo.byId(id);
		var input = dojo.byId(li.getAttribute("inputid")||null);
		input.checked = false;
		AutoCheck._updateDisplay(input);
	}
};

dojo.addOnLoad(function() {
	var ins = document.forms[AutoCheck.formName].getElementsByTagName("input");
	for(var i = 0; i < ins.length; i++) {
		var input = ins[i];
		if(input.type == "checkbox" && input.checked && input.getAttribute("date")) {
			AutoCheck._updateDisplay(input);
		}
	}
});
