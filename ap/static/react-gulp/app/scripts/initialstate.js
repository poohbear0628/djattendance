//initial state
var trainee = require("./testdata/trainee");
var events = require("./testdata/events");
var rolls = require("./testdata/rolls");
var slips = require("./testdata/slips");

var initialState = {
        trainee: trainee,
        events: events,
        rolls: rolls,
        slips: slips,
        date: moment(),
        selectedEvents: []
    };

module.exports = initialState;