var trainee = require("./testdata/trainee");
var trainees = require("./testdata/trainees");
var tas = require("./testdata/tas");
var events = require("./testdata/events-small");
var rolls = require("./testdata/rolls");
var iSlips = require("./testdata/individualSlips");
var gSlips = require("./testdata/groupSlips");
var term = require("./testdata/term");

//see attendance_react.html
if (typeof Trainee !== 'undefined') {
  if (Trainee.constructor === Array) {
    trainee = Trainee[0];
  } else {
    trainee = Trainee;
  } 
}
if (typeof Term !== 'undefined') {
  if (Term.constructor === Array) {
    term = Term[0];
  } else {
    term = Term;
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

var isSecondYear = trainee.terms_attended[trainee.terms_attended.length-1] <= 2 ? true : false;

//debug purposes only!!
var STARTINGDATE = new Date();
STARTINGDATE.setDate(STARTINGDATE.getDate() - 10);


var initialState = {
  show: '',
  form: {
    rollStatus: {},
    leaveSlip: {
      comment: "",
      slipType: {},
      ta_informed: {},
      ta: {},
    },
    groupSlip: {
      comment: "",
      slipType: {},
      ta_informed: {},
      ta: {},
      trainees: [],
      start_time: null,
      end_time: null,
    }
  },
  selectedEvents: [],
  date: STARTINGDATE,
  toggle: {
    roll: false,
    leaveslip: false,
    groupslip: false
  },
  rolls: rolls,
  leaveslips: iSlips,
  groupslips: gSlips,
  
  
  events: events,
  trainee: trainee,
  trainees: trainees,
  isSecondYear: true,//isSecondYear, 
  tas: tas,
  term: term, 
  
  
  submitting: false,
  formSuccess: null,
  
};

console.log(initialState);

module.exports = initialState;