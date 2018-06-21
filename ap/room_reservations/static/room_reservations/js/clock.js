// this script was taken and edited from http://widget.time.is/en.js

// Init parameters
// Parameter        Valid keywords
// template         TIME, DATE, SUN
// time_format      hours, minutes, seconds, 12hours, AMPM
// date_format      dayname, dname, daynum, dnum, day_in_y, week, monthname, monthnum, mnum, yy, year
// sun_format       srhour, srminute, sr12hour, srAMPM, sshour, ssminute, ss12hour, ssAMPM, dlhours, dlminutes
// coords           The location's latitude and longitude. Required for displaying sun times and day length.   
// id               For identifying the location and the time zone on the server side. Required if the location name contains non-ascii letters, and if you change the HTML element id.    

// do not change this variable name, the time.is api relies on it
var time_is_widget = new time_is_widget();

function time_is_widget() {
    // variable initialization
    var config = 0, timeDiff = 0, timeout = 0, updint = 1000, U = "undefined";
    var p = {
        n: "Sunday.Monday.Tuesday.Wednesday.Thursday.Friday.Saturday.Sun.Mon.Tue.Wed.Thu.Fri.Sat.January.February.March.April.May.June.July.August.September.October.November.December",
        w: "week ",
        W: "week .n",
        dy: " day"
    };
    p["n"] = p["n"].split(".");

    this.init = function(config) {
        if (timeout != 0) {
            clearInterval(time_is_widget.timeout);
        }
        // see documentation at the top
        var q = [];
        var dateFormatMap = {
            dayname: "%l",
            dname: "%D",
            daynum: "%d",
            dnum: "%j",
            day_in_y: "%z",
            week: "%W",
            monthname: "%F",
            monthnum: "%m",
            mnum: "%n",
            yy: "%y",
            year: "%Y",
            "12hours": "%h",
            hours: "%H",
            minutes: "%i",
            seconds: "%s",
            AMPM: "%A"
        };
        // defaults
        var template = "TIME";
        var timeFormat = "%H:%i:%s";
        var dateFormat = "%Y-%d-%m";
        var sunFormat = "%srH:%srm-%ssH:%ssm";
        // this for loop is to allow for multiple times to be displayed based on how many locations you list in the config obj
        var subConfig;
        for (var id in config) {
            subConfig = config[id];
            subConfig["p"] = "";
            if (typeof subConfig["id"] == U) {
                subConfig["id"] = id;
            }
            if (typeof subConfig["time_format"] != U) {
                timeFormat = subConfig["time_format"];
            }
            if (typeof subConfig["date_format"] != U) {
                dateFormat = subConfig["date_format"];
            }
            if (typeof subConfig["sun_format"] != U) {
                sunFormat = subConfig["sun_format"];
            }
            for (var key in dateFormatMap) {
                dateFormat = dateFormat.replace(key, dateFormatMap[key]);
                timeFormat = timeFormat.replace(key, dateFormatMap[key]);
            }
            if (typeof subConfig["template"] != U) {
                template = subConfig["template"];
            }
            var time_html = '<div id="clock-container" class="row"><div class="col-sm-12"><span id="clock">' + timeFormat + '</span></div></div>';
            var date_html = '<div id="date-container" class="row"><div class="col-sm-12"><span id="date">' + dateFormat + '</span></div></div>';
            subConfig["template"] = template.replace("SUN", "<span>" + sunFormat + "</span>").replace("TIME", time_html).replace("DATE", date_html);
            if (typeof subConfig["vector"] == U) {
                q.push(subConfig["id"]);
                if (typeof subConfig["coords"] != U) {
                    q[q.length - 1] += "." + subConfig["coords"].replace(",", "_");
                }
            }
            config[id] = subConfig;
        }
        this.config = config;
        if (q.length > 0) {
            // this is where the magic happens, this is why we can't change the initial variable name
            // !!!!! IF OUR CLOCK BREAKS THIS IS WHY, WHAT THIS SCRIPT TAG LOADS WILL LOOK DIFFERENT THAN BELOW !!!!!
            // this script tag loads a one line script that looks something like:
            // time_is_widget.cb(1529542150750,1529542150486,[[-420,1541321999999,-480,0,0,0,0,0,0]])
            // the parameters passed into cb are most likely from the query parameters passed into the src url which looks something like:
            // http://widget.time.is/?Anaheim_z14e&t=1529542150486
            var scriptTag = document.createElement("script");
            scriptTag.setAttribute("src", "//widget.time.is/?" + encodeURIComponent(q.join("..")) + "&t=" + new Date().getTime());
            var headTag = document.getElementsByTagName("head").item(0);
            headTag.appendChild(scriptTag);
        } else {
            this.tick();
        }
    };

    this.cb = function(t, r, a) {
        var rpT = new Date()
        var n = 0;
        time_is_widget.timeDiff = rpT.getTime() - t - Math.round((rpT - r) / 2);
        for (var i in this.config) {
            this.config[i]["vector"] = a[n];
            n++;
        }
        this.tick();
    };

    this.tick = function() {
        var tU = new Date(), t = new Date(), c, pw;
        tU.setTime(tU.getTime() - this.timeDiff);
        // this for loop is to allow for multiple times to be displayed based on how many locations you list in the config obj
        for (i in this.config) {
            c = this.config[i];
            if (typeof c["vector"][0] != U) {
                if ((0 < c["vector"][1]) && (c["vector"][1] < tU.getTime())) {
                    c["vector"][0] = c["vector"][2];
                    c["vector"][1] = 0;
                }
                t.setTime(c["vector"][0] * 60000 + tU.getTime());
                var d;
                var y = t.getUTCFullYear() + "";
                var m = t.getUTCMonth() + 1
                var N = new Date(y,0,1);
                var o = N.getDay() - 1;
                if (o == -1) {
                    o = 6;
                }
                var W = Math.floor((t - N + N.getTimezoneOffset() * 60000) / 604800000 + (o / 7));
                var dn = p["dy"] + " " + Math.floor((t - N + N.getTimezoneOffset() * 60000) / 86400000 + 1);
                if (o < 4) {
                    W++;
                }
                if (W == 0) {
                    W = 52;
                    if (new Date(y - 1,0,1).getDay() == 4 || new Date(y - 1,11,31).getDay() == 4) {
                        W = 53;
                    }
                }
                pw = p["W"].replace(".n", W);
                var g = {
                    t: t.getUTCHours(),
                    r: c["vector"][3],
                    s: c["vector"][5]
                }
                  , h = {};
                for (var j in g) {
                    h[j] = addLeadingZero(g[j]);
                    h[j + "H"] = h[j];
                    h[j + "M"] = "AM";
                    if (11 < h[j]) {
                        h[j + "M"] = "PM";
                        h[j] = addLeadingZero(h[j] - 12);
                        if (h[j] == "00") {
                            h[j] = 12;
                        }
                    }
                }
                // see documentation at the top and the dateFormatMap in init
                d = c["template"]
                    .replace("srhour", h["rH"])
                    .replace("sr12hour", h["r"])
                    .replace("srAMPM", '<span id="ampm">' + h["rM"] + '</span>')
                    .replace("srminute", addLeadingZero(c["vector"][4]))
                    .replace("sshour", h["sH"])
                    .replace("ss12hour", h["s"])
                    .replace("ssAMPM", '<span id="ampm">' + h["sM"] + '</span>')
                    .replace("ssminute", addLeadingZero(c["vector"][6]))
                    .replace("dlhours", c["vector"][7])
                    .replace("dlminutes", c["vector"][8])
                    .replace("%H", h["tH"])
                    .replace("%h", h["t"])
                    .replace("%i", addLeadingZero(t.getUTCMinutes()))
                    .replace("%s", addLeadingZero(t.getUTCSeconds()))
                    .replace("%A", '<span id="ampm">' + h["tM"] + '</span>')
                    .replace("%j", t.getUTCDate())
                    .replace("%d", addLeadingZero(t.getUTCDate()))
                    .replace("%W", pw)
                    .replace("%n", m)
                    .replace("%m", addLeadingZero(m))
                    .replace("%y", y.substr(2, 2))
                    .replace("%Y", y)
                    .replace("%F", p["n"][13 + m])
                    .replace("%l", p["n"][t.getUTCDay()])
                    .replace("%D", p["n"][7 + t.getUTCDay()])
                    .replace("%z", dn);
                j = d.indexOf(">");
                d = d.substr(0, j + 1) + d.substr(j + 1, 1).toUpperCase() + d.substr(j + 2, d.length - 1);
                if (d != c["p"]) {
                    if (document.getElementById) {
                        o = document.getElementById(i);
                    }
                    else {
                        o = eval();
                    }
                    if (null != o) {
                        o.innerHTML = d;
                        c["p"] = d;
                    }
                }
            }
        }
        timeout = setTimeout('time_is_widget.tick()', updint - tU % updint);
    }

    function addLeadingZero(n) {
        return n > 9 ? n : "0" + n;
    }
}
