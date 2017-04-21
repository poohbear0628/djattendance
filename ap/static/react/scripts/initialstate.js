var trainee = require("./testdata/trainee");
var trainees = require("./testdata/trainees");
var tas = require("./testdata/tas");
var events = require("./testdata/events-small");
var rolls = require("./testdata/rolls");
var iSlips = require("./testdata/individualSlips");
var gSlips = require("./testdata/groupSlips");
var term = require("./testdata/term");
var groupevents = require("./testdata/groupevents");

//see attendance_react.html
if (typeof Trainee !== 'undefined') {
  if (Trainee.constructor === Array) {
    trainee = Trainee[0];
  } else {
    trainee = Trainee;
<<<<<<< HEAD
  }
=======
  } 
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
}
if (typeof Term !== 'undefined') {
  if (Term.constructor === Array) {
    term = Term[0];
  } else {
    term = Term;
<<<<<<< HEAD
  }
=======
  } 
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
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
if (typeof GroupEvents !== 'undefined') {
  groupevents = GroupEvents;
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

<<<<<<< HEAD
=======
var isSecondYear = trainee.terms_attended[trainee.terms_attended.length-1] <= 2 ? true : false;

//debug purposes only!!
var STARTINGDATE = new Date();
STARTINGDATE.setDate(STARTINGDATE.getDate() - 10);

>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
var initialState = {
  show: 'summary',
  form: {
    rollStatus: {},
    leaveSlip: {
      comment: "",
      slipType: {},
<<<<<<< HEAD
      ta_informed: {'id': 'true', 'name': 'TA informed:'},
=======
      ta_informed: {},
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
      ta: {},
    },
    groupSlip: {
      comment: "",
      slipType: {},
<<<<<<< HEAD
      ta_informed: {'id': 'true', 'name': 'TA informed:'},
=======
      ta_informed: {},
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
      ta: {},
      trainees: [],
      start_time: null,
      end_time: null,
<<<<<<< HEAD
    },
    traineeView: trainee,
  },
  selectedEvents: [],
  date: new Date(),
=======
    }
  },
  selectedEvents: [],
  date: STARTINGDATE,
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  toggle: {
    roll: false,
    leaveslip: false,
    groupslip: false
  },
  rolls: rolls,
  leaveslips: iSlips,
  groupslips: gSlips,
  groupevents: groupevents,
  events: events,
  trainee: trainee,
  trainees: trainees,
<<<<<<< HEAD
  tas: tas,
  term: term,
  
  submitting: false,
  formSuccess: null,

};

module.exports = initialState;
=======
  isSecondYear: true,//isSecondYear, 
  tas: tas,
  term: term, 
  
  
  submitting: false,
  formSuccess: null,
  
};

module.exports = initialState;
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
