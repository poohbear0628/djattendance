import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'

import { joinValidClasses } from '../constants'

class DaysRow extends Component {
  render() {
    var days = [];
    var week = dateFns.eachDay(dateFns.startOfWeek(this.props.date), dateFns.endOfWeek(this.props.date));
    for(var i = 0; i < 7; i++) {
      var name = dateFns.format(week[i], 'ddd');
      var num = dateFns.format(week[i], 'D');
      var isToday = dateFns.isSameDay(week[i], this.props.date);
      var today = isToday ? 'today' : '';
      var classes = joinValidClasses(['schedule-header', today]);
      days.push(
        <div className="col-md-1 no-padding days-row" key={i}>
          <div className={classes}>
            {name}  {num}
          </div>
        </div>
      );
    }
    return (
      <div>
        <div className="col-md-1">
          <div className="col-md-1 no-padding">
            <div className="schedule-header dead-space"></div>
          </div>
        </div>
        {days}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    date: state.date
  };
}

export default connect(
  mapStateToProps
)(DaysRow);