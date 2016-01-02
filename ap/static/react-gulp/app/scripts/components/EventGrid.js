import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import EventView from '../components/EventView'

import { joinValidClasses } from '../constants'

class EventGrid extends Component {
  render() {
    var cols = [],
        weekStart = dateFns.format(dateFns.startOfWeek(this.props.date), 'M/D/YY'),
        weekEnd = dateFns.format(dateFns.endOfWeek(this.props.date), 'M/D/YY'),
        now = new Date();

    console.log(this.props.events);
    var week_events = _.filter(this.props.events, function(ev) {
        // console.log(new Date(weekStart), new Date(ev['start']), (new Date(weekStart) < new Date(ev['start'])));
        return (new Date(weekStart) < new Date(ev['start']) && new Date(weekEnd) > new Date(ev['end']));
    }, this);

    console.log("week events", week_events);

    for (var i = 0; i < 7; i++) {
      var day_events = _.filter(week_events, function(ev) {
        return dateFns.getDay(ev['start']) === i;
      });

      var sorted = _.sortBy(day_events, 'start');

      var day_col = [];
      sorted.forEach(function(event) {
        day_col.push(<EventView event={event} slips={this.props.slips} rolls={this.props.rolls} selectedEvent={this.props.selectedEvent} key={event.id} />);
      }, this);

      // I do not understand the purpose of this... just setting it to false for now
      // original momentjs code
      // this.props.date.day(i).isSame(now, 'day');
      // datefns code
      // dateFns.getDay(this.props.date) == dateFns.getDay(now);
      var isToday = false;
      var today = isToday ? 'today' : '';
      var classes = joinValidClasses(['day event-col col-md-1 no-padding', today]);
      cols.push(<div key={i} className={classes}>{day_col}</div>);
    }

    return (
      <div>
        {cols}
      </div>
    );
  }
}

// Which part of the Redux global state does our component want to receive as props?
function mapStateToProps(state) {
  return {
    date: state.date,
    slips: state.slips,
    rolls: state.rolls,
    events: state.events,
    selectedEvent: state.selectedEvent
  };
}

export default connect(mapStateToProps)(EventGrid);
