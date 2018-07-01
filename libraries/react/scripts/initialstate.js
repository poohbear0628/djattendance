var trainee = require("./testdata/trainee");
var trainees = require("./testdata/trainees");
var tas = require("./testdata/tas");
var events = require("./testdata/events-small");
var rolls = require("./testdata/rolls");
var iSlips = require("./testdata/individualSlips");
var gSlips = require("./testdata/groupSlips");
var term = require("./testdata/term");
var groupevents = require("./testdata/groupevents");
var date = new Date();
var selectedEvents = [];
var show = 'summary';
var disablePeriodSelect = 0;

import { TA_IS_INFORMED, TA_EMPTY } from './constants'

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
if (typeof Today !== 'undefined') {
  date = Today;
}
if (typeof SelectedEvents !== 'undefined') {
  selectedEvents = SelectedEvents;
}
if (typeof Show !== 'undefined') {
  show = Show;
}
if (typeof DisablePeriodSelect !== 'undefined') {
  disablePeriodSelect = DisablePeriodSelect;
}

// form fields
var id = null;
var groupSlipTrainees = [];
var slipType = {};
var description = "";
var taComments = "";
var informed = TA_EMPTY;
var taInformed = TA_EMPTY;
var texted = null;
var taAssigned = TA_EMPTY;
var privateComments = "";

if ( typeof Id !== 'undefined') {
  id = Id;
}
if (typeof GroupSlipTrainees !== 'undefined') {
  groupSlipTrainees = GroupSlipTrainees;
}
if ( typeof SlipType !== 'undefined') {
  slipType = SlipType;
}
if ( typeof Description !== 'undefined') {
  description = Description;
}
if ( typeof TAComments !== 'undefined') {
  taComments = TAComments;
}
if ( typeof TAInformed !== 'undefined') {
  informed = TA_IS_INFORMED;;
  taInformed = TAInformed;
}
if ( typeof Texted !== 'undefined') {
  texted = Texted;
}
if ( typeof TAAssigned !== 'undefined') {
  taAssigned = TAAssigned;
}
if ( typeof PrivateComments !== 'undefined') {
  privateComments = PrivateComments;
}

var initialState = {
  show: show,
  form: {
    rollStatus: {},
    leaveSlip: {
      description: "",
      slipType: {},
      informed: TA_EMPTY,
      ta: TA_EMPTY,
      id: null,
    },
    groupSlip: {
      description: description,
      slipType: slipType,
      informed: informed,
      taInformed: taInformed,
      taAssigned: taAssigned,
      trainees: groupSlipTrainees,
      id: id,
      taComments: taComments,
      privateComments: privateComments,
      texted: texted,
    },
    traineeView: trainee,
  },
  selectedEvents: selectedEvents,
  date: date,
  rolls: rolls,
  leaveslips: iSlips,
  groupslips: gSlips,
  groupevents: groupevents,
  events: events,
  trainee: User || trainee,
  trainees: trainees,
  tas: tas,
  term: term,
  showLegend: true,
  disablePeriodSelect: disablePeriodSelect,
  isTAView: isTAView,

  submitting: false,
  formSuccess: null,
};

export default initialState;
