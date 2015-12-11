var Event = Backbone.Model.extend({
  urlRoot: '/api/event',
  addRollID: function(rollID) {
    this.set({
      roll: rollID
    });
  },
  addSlipID: function(slipID) {
    this.set({
      slip: slipID
    });
  }
});

var Roll = Backbone.Model.extend({
  urlRoot: '/api/rolls/'
});

var LeaveSlip = Backbone.Model.extend({
  urlRoot: '/api/leaveslips/'
});
