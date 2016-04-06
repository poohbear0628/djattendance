// This function gets the value of a parameter specified in the URL
function getParameter( name ) {
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( window.location.href );
    if ( results == null ) {
        return "";
    } else { 
        return unescape(results[1]);
    }
}

var WeekSelector = {
    url: "../../schedule/getWeek.php",
    active: null,
    init: function() {
        var weeks = dojo.byId("weeks");
        if(!weeks) {
            return;
        }
        var a = weeks.getElementsByTagName("a");
        for(var i = 0; i < a.length; i++) {
            dojo.event.connect(a[i], "onclick", this, "onclick");
            if (dojo.html.hasClass(a[i], "active") ) {
                this.select(a[i]);
                this.active = a[i];
            } // if

            // For allweeks pre-click to load all the weeks stacked vertically
            if ((getParameter("allweeks") == "true")	&& (a[i].href.indexOf("#mon") > 0)) {
                this.select(a[i]);
                // remove the tabs when we are vertically stacking them
                // the tabs get really wide and ugly, and they don't do anything
                a[i].style.display='none';
            }		    
			
        } // for
	   
		
    }, // init 

    onclick: function(e) {
        e.preventDefault();
        this.select(e.currentTarget);
    },

    weekFromNode: function(node) {
        var re = (node.href||"").match(/mon(\d+)$/);
        if(!re) {
            return -1;
        }
        return week = re[1];
    },
	
    onShow: function(week) {},

    showWeek: function(week) {
        this.hideLoading();
		
        // If this is an allweeks leave slip, then we won't swap any views
        // This will cause all the weeks to 'stack' on top of each other
        // this is very convenient for attendance monitors
        if (getParameter("allweeks") == "true") {
            return;
        }
		
        // assume we won't have more than 2 weeks (any more and we'll stack them)
        for(var i = 1; i <=2; i++) {
            var node = dojo.byId("week"+i);
			
            $("#weeks > li > a").removeClass("active"); //remove all active in weeks
            $("#weeks > li:eq("+(week-1)+") > a").addClass("active"); // add active in the current week
      
            if(!node) {
                continue;
            }
            if(week == i) {
                node.style.display = "block";

                //var mondaytab = startmonday + ((i-1) * (7*24*60*60))
                //the following is DST safe
                // NOTE : the addition of 10 hours will cause this not to break (choose the wrong day)
                // when the client is off by a couple of hours due to bad time zone settings or incorrect DST settings
                var jsStartMonday = new Date((startmonday * 1000) + 36000000);
                jsStartMonday.setDate(jsStartMonday.getDate() + (i-1) * 7);
                var mondaytab = jsStartMonday.getTime() / 1000;

                var tab = dojo.byId("week-tab" + mondaytab);
				
                if(this.active && this.active != tab) {
                //dojo.html.removeClass(this.active, "active"); // this code doesn't work...
                }
				
                this.active = tab;
                this.onShow(week);
            } else {
                node.style.display = "none";
            }
        }
    },

    showLoading: function() {
        this.showWeek();
        try {
            dojo.byId("loading-week").style.display = "block";
        } catch(E) {}
    },

    hideLoading: function() {
        try {
            dojo.byId("loading-week").style.display = "none";
        } catch(E) {}
    },

    select: function(node) {
        var weeknumber = this.weekFromNode(node);
        //var mondaytoshow = startmonday + ((weeknumber-1) * (7*24*60*60));
        //the following is DST safe
        // NOTE : the addition of 10 hours will cause this not to break (choose the wrong day)
        // when the client is off by a couple of hours due to bad time zone settings or incorrect DST settings
        var jsStartMonday = new Date((startmonday * 1000)  + 36000000);
        jsStartMonday.setDate(jsStartMonday.getDate() + (weeknumber-1) * 7);
        var mondaytoshow = jsStartMonday.getTime() / 1000;

        // create a new node to store the location of the ajax loaded week
        // This will prevent server response order from interefering with the order on the page
        var newWeekDivHTML = "<div id='newdate_"+mondaytoshow+"'></div>";
        var newWeekDiv = dojo.html.createNodesFromText(newWeekDivHTML, true)[0];
        dojo.byId("cal-container").appendChild(newWeekDiv);
	
        if (weeknumber < 0) {
            return;
        }

        if (dojo.byId("week" + weeknumber)) {
            this.showWeek(weeknumber);
        } else {
            this.showLoading();
            dojo.io.bind({
                url: this.url,
                content: {
                    monday: mondaytoshow, 
                    userid: userid, 
                    weeknumber: weeknumber, 
                    arrayname: arrayname
                },
                load: dojo.lang.hitch(this, function(type, data) {
                    if($("#newdate_"+mondaytoshow).children().length==0){
                        var box = dojo.html.createNodesFromText(data, true)[0];
                        // Store the data from the server into the div created for it
                        dojo.byId("newdate_"+mondaytoshow).appendChild(box);
                        if (dojo.byId("newdate_"+mondaytoshow) == null) alert("Not found newdate_"+mondaytoshow);
                        this.showWeek(weeknumber);
                        this.onLoad(weeknumber);
                        this.loadDefaults();
                    }
                })
            });
        }
    },
	
    onLoad: function(weeknumber) {},
	
    loadDefaults: function() {}
};

dojo.addOnLoad(function() {
    WeekSelector.init();
});
