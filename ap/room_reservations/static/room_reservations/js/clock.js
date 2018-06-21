// taken and edited from http://widget.time.is/en.js

// do not change this variable name, the time.is api relies on it
var time_is_widget = new time_is_widget();

function time_is_widget() {
    // variable initialization
    var i, j;
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
        var a, q = [], c = {
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
        var template = "TIME";
        var timeFormat = "%H:%i:%s";
        var dateFormat = "%Y-%d-%m";
        var sunFormat = "%srH:%srm-%ssH:%ssm";
        // this for loop is to allow for multiple times to be displayed based on how many locations you list in the config obj
        for (i in config) {
            console.log("i", i);
            a = config[i];
            console.log("a", a);
            a["p"] = "";
            if (typeof a["id"] == U) {
                a["id"] = i;
            }
            if (typeof a["time_format"] != U) {
                timeFormat = a["time_format"];
            }
            if (typeof a["date_format"] != U) {
                dateFormat = a["date_format"];
            }
            if (typeof a["sun_format"] != U) {
                sunFormat = a["sun_format"];
            }
            console.log("c", c);
            for (j in c) {
                dateFormat = dateFormat.replace(j, c[j]);
                timeFormat = timeFormat.replace(j, c[j]);
            }
            console.log("dateFormat", dateFormat);
            console.log("timeFormat", timeFormat);
            if (typeof a["template"] != U) {
                template = a["template"];
            }
            var time_html = '<div id="clock-container" class="row"><div class="col-sm-12"><span id="clock">' + timeFormat + '</span></div></div>';
            var date_html = '<div id="date-container" class="row"><div class="col-sm-12"><span id="date">' + dateFormat + '</span></div></div>';
            a["template"] = template.replace("SUN", "<span>" + sunFormat + "</span>").replace("TIME", time_html).replace("DATE", date_html);
            if (typeof a["vector"] == U) {
                q.push(a["id"]);
                if (typeof a["coords"] != U) {
                    console.log(8)
                    q[q.length - 1] += "." + a["coords"].replace(",", "_");
                }
            }
            config[i] = a;
            console.log("a", a);
        }
        this.config = config;
        console.log("q", q);
        if (q.length > 0) {
            // this is where the magic happens, this is why we can't change the initial variable name
            // this script tag loads a one line script that looks something like:
            // time_is_widget.cb(1529542150750,1529542150486,[[-420,1541321999999,-480,0,0,0,0,0,0]])
            // the parameters passed into cb are most likely from the query parameters passed into the src url which looks something like:
            // http://widget.time.is/?Anaheim_z14e&t=1529542150486
            i = document.createElement("script");
            i.setAttribute("src", "//widget.time.is/?" + encodeURIComponent(q.join("..")) + "&t=" + new Date().getTime());
            j = document.getElementsByTagName("head").item(0);
            j.appendChild(i);
            console.log("i", i);
        } else {
            this.tick();
        }
    };

    this.cb = function(t, r, a) {
        console.log('cb');
        var rpT = new Date()
        var n = 0;
        time_is_widget.timeDiff = rpT.getTime() - t - Math.round((rpT - r) / 2);
        console.log("cb config", this.config);
        for (i in this.config) {
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
                var W = Math.floor((t - N + N.getTimezoneOffset() * 60000) / 604800000 + (o / 7)),
                    dn = p["dy"] + " " + Math.floor((t - N + N.getTimezoneOffset() * 60000) / 86400000 + 1);
                if (o < 4) {
                    W++;
                }
                if (W == 0) {
                    W = 52;
                    if (new Date(y - 1,0,1).getDay() == 4 || new Date(y - 1,11,31).getDay() == 4) {
                        W = 53;
                    }
                }
                if (p["W"] == "hy") {
                    if (W == 1) {
                        pw = "1-ին շաբաթ";
                    }
                    else {
                        pw = W + "-րդ շաբաթ";
                    }
                } else {
                    pw = p["W"].replace(".n", W);
                }
                var g = {
                    t: t.getUTCHours(),
                    r: c["vector"][3],
                    s: c["vector"][5]
                }
                  , h = {};
                for (j in g) {
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
                    .replace("%h", h["t"])
                    .replace("%H", h["tH"])
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
            if (typeof c["callback"] != U) {
                eval(c["callback"] + "(d)");
            }
        }
        timeout = setTimeout('time_is_widget.tick("")', updint - tU % updint);
    }

    function addLeadingZero(n) {
        return n > 9 ? n : "0" + n;
    }
}
