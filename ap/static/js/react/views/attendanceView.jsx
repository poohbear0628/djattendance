var Attendance = React.createClass({
  mixins: [
    Reflux.connect(attendanceStore)
  ],
  render: function() {
    console.log('render attendance');
    return (
    <div>
      <div>
        <Trainee
          trainee={this.state.trainee}
        />
        <WeekBar
          date={this.state.date}
        />
        <hr />
        <div className="row">
          <DaysRow date={this.state.date} />
        </div>
        <div className="row">
          <TimesColumn />
          <EventGrid
            events={this.state.events}
            rolls={this.state.rolls}
            slips={this.state.slips}
            date={this.state.date}
          />
          <div className="col-md-4 action-col">
            <RollView
              selectedEvents={this.state.selectedEvents}
            />
          </div>
        </div>
      </div>
      <hr />
    </div>
    );
  }
});
