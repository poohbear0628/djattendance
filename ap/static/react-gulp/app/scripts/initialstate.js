var trainee = require("./testdata/trainee");
var trainees = require("./testdata/trainees");
var tas = require("./testdata/tas")
var events = require("./testdata/events");
var rolls = require("./testdata/rolls");
var iSlips = require("./testdata/individualSlips");
var gSlips = require("./testdata/groupSlips")

//see attendance_react.html
if (typeof Trainee !== 'undefined') {
  if (Trainee.constructor === Array) {
    trainee = Trainee[0];
  } else {
    trainee = Trainee;
  } 
}
if (typeof Trainees !== 'undefined') {
  trainees = Trainees;
}
if (typeof TAs !== 'undefined') {
  tas = TAs;
}
if (typeof Events !== 'undefined') {
  events = Events;
}
if (typeof Rolls !== 'undefined') {
  rolls = Rolls;
}
if (typeof IndividualSlips !== 'undefined') {
  iSlips = IndividualSlips;
}
if (typeof GroupSlips !== 'undefined') {
  gSlips = GroupSlips;
}

var isSecondYear = true
if (trainee.terms_attended[trainee.terms_attended.length-1] <= 2) {
  var isSecondYear = false;
}

//combine events and slips
var events_slips = [];
for (var i = 0; i < events.length; i++) {
  var ev = events[i];
  var event_slip = { event : ev,
                     slip  : null,
                     gslip : null, }
  for (var j = 0; j < iSlips.length; j++) {
    var sl = iSlips[j];
    for (var k = 0; k < sl.events.length; k++) {
      if (ev.id == sl.events[k].id && dateFns.format(ev.start, 'YYYY-MM-DD') == sl.events[k].date) {
        event_slip.slip = sl;
        break;
      }
    }

    if (event_slip.slip) {
      break;
    }
  }

  for (var j = 0; j < gSlips.length; j++) {
    var gsl = gSlips[j];
    if (ev.start >= gsl.start && ev.start <= gsl.end) {
      event_slip.gslip = gsl;
      break;
    }
  }

  events_slips.push(event_slip);
}

//combine events and slips and rolls
var events_slips_rolls = [];
for (var i = 0; i < events_slips.length; i++) {
  var ev = events_slips[i].event;
  var sl = events_slips[i].slip;
  var gsl = events_slips[i].gslip;
  var event_slip_roll = { event : ev,
                          slip  : sl,
                          gslip : gsl,
                          roll  : null }
  for (var j = 0; j < rolls.length; j++) {
    if (ev.id == rolls[j].event && dateFns.format(ev.start, 'YYYY-MM-DD') == rolls[j].date) {
      event_slip_roll.roll = rolls[j];
      break;
    }
  }

  events_slips_rolls.push(event_slip_roll);
}

//collapse status of each LeaveSlipDetail
var leaveSlipDetailsShow = {};
for (var i = 0; i < iSlips.length; i++) {
  leaveSlipDetailsShow[iSlips[i].id] = false;
}

var groupSlipDetailsShow = {};
for (var i = 0; i < gSlips.length; i++) {
  groupSlipDetailsShow[gSlips[i].id] = false;
}

var initialState = {
    form: {
      rollSlipForm: {},
      groupLeaveSlipForm: {},
    },
    reducer: {
      trainee: trainee,
      trainees: trainees,
      isSecondYear: isSecondYear, 
      tas: tas,
      events: events,
      rolls: rolls,
      slips: iSlips,
      gslips: gSlips,
      eventsSlipsRolls: events_slips_rolls,
      date: new Date(),
      selectedEvents: [],
      leaveSlipDetailsShow: leaveSlipDetailsShow,
      leaveSlipDetailFormValues: {
            slipType: "",
            comments: "",
            informed: "true",
            TAInformed: ""
          },
      groupSlipDetailsShow: groupSlipDetailsShow,
      groupSlipDetailFormValues: {
          trainees: "",
            slipType: "",
            comments: "",
            informed: "true",
            TAInformed: ""
          },
      unexcusedAbsencesShow: true,
      unexcusedTardiesShow: true,
      excusedShow: true,
      submitRollShow: false,
      submitLeaveSlipShow: false,
      submitGroupLeaveSlipShow: false,
      leaveSlipsShow: false,
      otherReasonsShow: false,
      submitting: false,
      formSuccess: null,
    }
  };

module.exports = initialState;