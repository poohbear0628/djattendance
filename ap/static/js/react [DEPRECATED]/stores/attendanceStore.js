/* global Trainee */

var attendanceStore = Reflux.createStore({
  listenables: [actions],

  getInitialState: function() {
    this.state = {
      events: {},
      trainee: trainee,
      date: moment(),
      selectedEvents: {},
      weekEvents: []
    };
    return this.state;
  },
  initEvents: function() {
    //Events should include last roll data into it
    //request.get('api/events/?trainee=[id]').end(function(){
    //  this.state.events = res;
    //});
  },
  handleDate: function(input) {
    var delta = (input === 'prev') ? -7 : 7;
    this.state.date.add('d', delta);
    this.trigger(this.state);
  },
  onNextWeek: function() {
    this.handleDate('next');
  },
  onPrevWeek: function() {
    this.handleDate('prev');
  },
  onToggleEvent: function(ev) {
    // Add remove selected events based on toggle
    if (!(ev.id in this.state.selectedEvents)) {
      ev.set('selected', 'selected-event');
      this.state.selectedEvents[ev.id] = ev;
    } else {
      ev.set('selected', '');
      delete this.state.selectedEvents[ev.id];
    }
    this.trigger(this.state);
  },
  setRollStatus: function(status) {
    if (_.size(this.state.selectedEvents) <= 0) {
      alert('Please select at 1 event before updating the status');
      return false;
    }
    //require('underscore');
    // send an array of [ev_id, trainee_id, roll_status];
    // roll id can be null, in which case, we need to create a new roll for the event
    var event_ids = _.map(this.state.selectedEvents, function(event) {
      return [event.id, this.state.trainee, event.roll.id]
    });
    request.post('/api/rolls/batch').send(event_ids).end(function() {
      // unselect all the events
      this.state.selectedEvents = {};
    });
  }
})