var Attendance = React.createClass({displayName: "Attendance",
  mixins: [
    Reflux.connect(attendanceStore)
  ],
  render: function() {
    console.log('render attendance');
    return (
    React.createElement("div", null, 
      React.createElement("div", null, 
        React.createElement(WeekBar, {
          date: this.state.date}
        ), 
        React.createElement("hr", null), 
        React.createElement("div", {className: "row"}, 
          React.createElement(DaysRow, {date: this.state.date})
        ), 
        React.createElement("div", {className: "row"}, 
          React.createElement(TimesColumn, null), 
          React.createElement(EventGrid, {
            events: this.state.events, 
            rolls: this.state.rolls, 
            slips: this.state.slips, 
            date: this.state.date}
          ), 
          React.createElement("div", {className: "col-md-4 action-col"}, 
            React.createElement(RollView, {
              selectedEvents: this.state.selectedEvents}
            )
          )
        )
      ), 
      React.createElement("hr", null)
    )
    );
  }
});
