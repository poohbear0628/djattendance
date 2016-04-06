/* Roll Picker
 *
 * Author: David Schontzler
 *
 * Used for selecting which roll(s) you want to enter attendance data for.
 * Used in David Combiths roll pages, especially:
 *  - rollDataEntry.php
 *  - period.php
**/

/* SELECTING PERIODS.
************************************/

var PeriodSelector = {
	url: "print-period.wrapper.php",
	currentPeriod:-1,

	init: function() {
		var periods = dojo.byId("periods");
		var a = periods.getElementsByTagName("a");
		for(var i = 0; i < a.length; i++) {
			dojo.event.connect(a[i], "onclick", this, "onclick");
			if(dojo.html.hasClass(a[i], "active")) {
				this.select(a);
				this.currentPeriod=i
			}
		}
		SchedEventCheckBoxes.grabPageData()
	},

	onclick: function(e) {
		e.preventDefault();
		this.select(e.currentTarget);
	},

	periodFromNode: function(node) {
		var re = (node.href||"").match(/period(\d+)$/);
		if(!re) { return -1; }
		return period = re[1];
	},
	
	showPeriod: function(period) {
		try{dojo.byId("period"+period).style.display="block"}catch(e){}
		
		dojo.html.addClass(dojo.byId("period-tab"+period), "active")
		this.currentPeriod = period;
		dojo.byId("period-container").scrollTop = 0;
	},
	
	hidePeriod: function(period) {
		try{dojo.byId("period"+period).style.display="none"}catch(e){}
		
		dojo.html.removeClass(dojo.byId("period-tab"+period), "active")
	},

	showLoading: function() {
		dojo.byId("loading-period").style.display = "block";
	},

	hideLoading: function() {
		dojo.byId("loading-period").style.display = "none";
	},

	select: function(node) {
		var period = this.periodFromNode(node);
		if(period < 0) { return; }

		if(dojo.byId("period" + period)) {
			this.hidePeriod(this.currentPeriod)
			this.showPeriod(period);
		} else {
			this.hidePeriod(this.currentPeriod)
			this.showLoading();
			dojo.io.bind({
				url: this.url,
				content: {period: period},
				load: dojo.lang.hitch(this, function(type, data) {
					var box = dojo.html.createNodesFromText(data, true)[0];
					if(!box.innerHTML)alert("Cannot load "+this.url);
					var pc = dojo.byId("period-container");
					pc.appendChild(box);
					this.hideLoading()
					this.showPeriod(period);
					
					// Register all checkboxes.
					SchedEventCheckBoxes.grabPageData()
				})
			});
		}
	}
};

dojo.addOnLoad(function() { PeriodSelector.init(); });

/* SCHEDULE EVENT GROUPS.
************************************/

// Group recognition functions.
var RecogGroup={
	// If you change any of these arrays, you have to make sure that
	// the rest of the arrays also correspond correctly.
	groupNames: ['house', 'team', 'meal', 'others'],
	
	groupNumbers: {house:0, team:1, meal:2, others:3},
	
	regexes: [
		/\b((Rise)|(Curfew)|(Bed)|(House))\b/,
		/\b((Work)|(Team)|(Prayer Meeting)|(Campus)|(Table)|(CP)|(YPC)|(COM))\b/,
		/\b((Breakfast)|(Lunch)|(Dinner))\b/,
		/.*/
	],
	
	// Return group name.
	getGroupName: function(s) {
		var i
		for(i=this.regexes.length-2;i>=0;i--) { // -2 to skip 'others'
			if(this.regexes[i].test(s))return this.groupNames[i]
		}
		return 'others'
	}
}

/* SCHEDULE EVENT CHECKBOXES.
************************************/

var SchedEventCheckBoxes={
	periods: [],
	periodGroups: [],
	days: [],
	periodSchedules: [],
	checkboxes: [],

	// Add a checkbox to the universal collection.
	add: function(schedEventCheckBoxObj) {
		var obj=schedEventCheckBoxObj
		
		// Group by period.
		if(!this.periods[obj.period])
			this.periods[obj.period]=[]
		this.periods[obj.period].push(obj)
		
		// Group by period and check-group.
		if(!this.periodGroups[obj.period])
			this.periodGroups[obj.period]=[]
		if(!this.periodGroups[obj.period][obj.group])
			this.periodGroups[obj.period][obj.group]=[]
		this.periodGroups[obj.period][obj.group].push(obj)
		
		// Group by day.
		if(!this.days[obj.date])
			this.days[obj.date]=[]
		this.days[obj.date].push(obj)
		
		// Group by period and schedule.
		if(!this.periodSchedules[obj.period])
			this.periodSchedules[obj.period]=[]
		if(!this.periodSchedules[obj.period][obj.schedule])
			this.periodSchedules[obj.period][obj.schedule]=[]
		this.periodSchedules[obj.period][obj.schedule].push(obj)
		
		// All checkboxes.
		this.checkboxes[obj.id]=obj
	},

	// Grab value and remove element.
	grabRid: function(id) {
		var o=document.f[id]
		var v=o.value
		try{o.parentNode.removeChild(o)}catch(e){}
		return v
	},
	
	// Grab all the checkbox data from the entire page.
	grabPageData: function() {
		var i,a=document.getElementsByTagName("input")
		for(i=a.length-1;i>=0;i--) {
			var o=a[i]
			if(o.className!='ckboxData')continue
			var id=o.value
			o.className='' // annihilate it
			o.parentNode.removeChild(o)
			
			var period=this.grabRid(id+"_period")
			var name=this.grabRid(id+"_eventName")
			var schedule=this.grabRid(id+"_schedule")
			var date=this.grabRid(id+"_date")
			var wday=this.grabRid(id+"_wday")
			var time=this.grabRid(id+"_time")
			var o=new SchedEventCheckBox(period,id,name,schedule,date,wday,time)
			this.add(o)
		}
	},

	// Click action.
	click: function(id) {
		this.checkboxes[id].click()
	},
	
	// Set the value of a checkbox, with complete screen update.
	check: function(id,bool) {
		var obj=this.checkboxes[id]
		if(obj.ckbox.checked!=bool){obj.ckbox.checked=bool;obj.click()}
	},
	
	// Check entire given array of checkboxes.
	checkArray: function(a,bool,update) {
		if(!a)return
		var i
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			if(obj.ckbox.checked!=bool) {
				obj.ckbox.checked=bool
				obj.clickNoUpdate()
			}
		}
		if(update)SelectedRolls.updateDisplay()
	},
	
	// Toggle entire given array of checkboxes.
	toggleArray: function(a,update) {
		if(!a)return
		var i
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			obj.ckbox.checked=!obj.ckbox.checked
			obj.clickNoUpdate()
		}
		if(update)SelectedRolls.updateDisplay()
	},
	
	// Set boolean value of entire period.
	checkPeriod: function(period,bool) {
		this.checkArray(this.periods[period],bool,1)
	},
	
	// Set boolean value of entire period.
	togglePeriod: function(period) {
		this.toggleArray(this.periods[period],1)
	},
	
	// Check one day.
	checkDay: function(day,bool) {
		this.checkArray(this.days[day],bool,1)
	},
	
	// Toggle one day.
	toggleDay: function(day) {
		this.toggleArray(this.days[day],1)
	},
	
	// Check one group, confined within a period.
	checkPeriodGroup: function(period,group,bool) {
		if(!this.periodGroups[period])return
		this.checkArray(this.periodGroups[period][group],bool,1)
	},

	// Toggle one group, confined within a period.
	togglePeriodGroup: function(period,group) {
		if(!this.periodGroups[period])return
		this.toggleArray(this.periodGroups[period][group],1)
	},
	
	// Check all groups, confined within a period.
	// Same as checkPeriod(), except that it also checks the auto-checkers.
	checkAllPeriodGroups: function(period,bool) {
		// Check the auto-check checkboxes.
		var i
		for(i=RecogGroup.groupNames.length-1;i>=0;i--) {
			var group=RecogGroup.groupNames[i]
			var ckbox=document.f["group_"+period+"_"+group]
			ckbox.checked=bool
		}
		
		// Same as checkPeriod() here.
		this.checkPeriod(period,bool)
	},

	// Toggle all group, confined within a period.
	// Different from togglePeriod().
	toggleAllPeriodGroups: function(period) {
		if(!this.periodGroups[period])return
		var i
		for(i=RecogGroup.groupNames.length-1;i>=0;i--) {
			var group=RecogGroup.groupNames[i]
			var ckbox=document.f["group_"+period+"_"+group]
			var bool=ckbox.checked=!ckbox.checked
			this.checkArray(this.periodGroups[period][group],bool,0)
		}
		SelectedRolls.updateDisplay()
	},
	
	// Show/hide schedules within given period.
	showHidePeriodSchedule: function(period,schedule,showHide) {
		if(!this.periodSchedules[period])return
		var a=this.periodSchedules[period][schedule]
		if(!a)return
		var i,bool=showHide?true:false,showHide=showHide?"":"none"
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			obj.visible=bool
			var li=document.getElementById("li_"+obj.id)
			li.style.display=showHide
		}
	},
	
	// Show/hide all schedules within given period.
	showHidePeriodSchedules: function(period,showHide) {
		// Check all auto-check boxes.
		a=document.getElementsByTagName("input")
		var pre="sched_"+period+"_"
		var len=pre.length
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			if(obj.type!='checkbox'||obj.name.substr(0,len)!=pre)
				continue
			obj.checked=bool
		}
		
		// Check/clear every checkbox.
		if(!this.periods[period])return
		var a=this.periods[period]
		var i,bool=showHide?true:false,showHide=showHide?"":"none"
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			obj.visible=bool
			var li=document.getElementById("li_"+obj.id)
			li.style.display=showHide
		}
	},

	// Show/hide all schedules within given period.
	togglePeriodSchedules: function(period) {
		// Check all auto-check boxes.
		a=document.getElementsByTagName("input")
		var pre="sched_"+period+"_"
		var len=pre.length
		for(i=a.length-1;i>=0;i--) {
			var obj=a[i]
			if(obj.type!='checkbox'||obj.name.substr(0,len)!=pre)
				continue
			var bool=obj.checked=!obj.checked
			
			var schedule=obj.name.substr(len)
			this.showHidePeriodSchedule(period,schedule,bool)
		}
	}	
};

SchedEventCheckBox = function(period,id,name,schedule,date,wday,time,bool) {
	// Save given values.
	this.period=period
	this.id=id
	this.name=name
	this.schedule=schedule
	this.date=date // `yyyymmdd'
	this.wday=wday // `Mon'
	this.time=time // `hh:mm[ap]m'

	// Other stuff.
	this.group=RecogGroup.getGroupName(this.name)
	this.ckbox=document.getElementById("check"+this.id)
	this.ckbox.checked=bool?true:false
	this.visible=true
}

SchedEventCheckBox.prototype.checked=function() {
	return this.ckbox.checked
}

SchedEventCheckBox.prototype.getDescription=function(wantDate) {
	return this.name
	  +" ("
	  +(wantDate?this.wday+" "+this.date.substr(4,2)+"/"+this.date.substr(6,2)+" @ ":"")
	  +this.time+")"
}

SchedEventCheckBox.prototype.clickNoUpdate=function() {
	if(!this.visible)return
	if(this.ckbox.checked==true)
		SelectedRolls.addNoUpdate(this.ckbox,this.getDescription(1))
	else
		SelectedRolls.removeNoUpdate(this.ckbox)
}

SchedEventCheckBox.prototype.click=function() {
	if(!this.visible)return
	if(this.ckbox.checked==true)
		SelectedRolls.add(this.ckbox,this.getDescription(1))
	else
		SelectedRolls.remove(this.ckbox)
}

SchedEventCheckBox.prototype.hide=function() {
	if(!this.visible)return
	this.visible=false
	if(!this.listObj)this.listObj=document.getElementById("li_"+this.id)
	this.listObj.style.display="none"
}

SchedEventCheckBox.prototype.show=function() {
	if(this.visible)return
	this.visible=true
	if(!this.listObj)this.listObj=document.getElementById("li_"+this.id)
	this.listObj.style.display=""
}

/* SELECTING ROLL CALLS.
************************************/

var SelectedRolls = {
	list: null,
	
	init: function() {
		var rolls = dojo.byId("selected-rolls");
		if(!rolls)return

		this.list = rolls.getElementsByTagName("ul")[0]
		this.updateDisplay()
	},

	updateDisplay: function() {
		var cnt = this.selectionCount();
		if(cnt == 0) {
			dojo.byId("selected-rolls-none").style.display = "block";
			dojo.byId("roll-picker-submit").disabled = true;
			dojo.byId("selected-rolls-count").innerHTML = "";
		} else {
			dojo.byId("selected-rolls-none").style.display = "none";
			dojo.byId("roll-picker-submit").disabled = false;
			dojo.byId("selected-rolls-count").innerHTML = " (" + cnt + ")";
		}
	},

	getObj: function(ckbox) {
		return dojo.byId(ckbox.id + "-selected")
	},

	addNoUpdate: function(ckbox, txt) {
		var entry = this.getObj(ckbox);
		if(entry)return
		var html = '<li id="' + ckbox.id + '-selected">'
			 + '<a class=remove title="Remove roll" for="'+ckbox.id
			 + '">x</a> ' + txt + '</li>';
		entry = dojo.html.createNodesFromText(html, true)[0];
		dojo.event.connect(entry.firstChild, "onclick", this, "uncheck");
		this.list.appendChild(entry);
	},

	add: function(ckbox, txt) {
		this.addNoUpdate(ckbox, txt)
		this.updateDisplay()
	},

	removeNoUpdate: function(ckbox) {
		var entry = this.getObj(ckbox);
		if(entry) entry.parentNode.removeChild(entry)
	},

	remove: function(ckbox) {
		this.removeNoUpdate(ckbox)
		this.updateDisplay();
	},

	selectionCount: function() {
		return this.list.getElementsByTagName("li").length - 1;
	},

	uncheck: function(e) {
		e.preventDefault();
		var entry = e.currentTarget;
		var id = entry.getAttribute("for");
		var ckbox=dojo.byId(id)
		ckbox.checked=false
		this.remove(ckbox)
	}
};

dojo.addOnLoad(function() { SelectedRolls.init(); });

/* SCHEDULE FILTER TOGGLER.
************************************/

function show_hide_ids(s,h)
{
  document.getElementById(h).style.display="none"
  document.getElementById(s).style.display="block"
}

/* SELECT TRAINEES BY YEAR/GENDER.
************************************/

var TraineeFilters = {
	chkall: function(v) {
	  document.f['1b'].checked=document.f['1s'].checked
	    =document.f['2b'].checked=document.f['2s'].checked=v
	},
	
	tgall: function(v) {
	  document.f['1b'].checked=!document.f['1b'].checked
	  document.f['1s'].checked=!document.f['1s'].checked
	  document.f['2b'].checked=!document.f['2b'].checked
	  document.f['2s'].checked=!document.f['2s'].checked
	},
	
	chkone: function(v) {
	  this.chkall(false)
	  document.f[v].checked=true
	}
};
