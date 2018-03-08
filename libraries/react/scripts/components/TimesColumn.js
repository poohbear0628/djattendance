import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

class TimesColumn extends Component {
  render() {
    var times = [];
    for (var i = 6; i < 24; i++) {
      var hour = "";
      if (i < 12) {
        hour += i.toString() + " AM";
      } else if (i == 12) {
        hour += i.toString() + " PM";
      } else {
        var j = i - 12
        hour += j.toString() + " PM";
      }

      times.push(
        <div key={i} className="cal-time__hour">
          <div className="hour-text" id={i}>{hour}</div>
        </div>
      );
    }
    return (
      <div className="cal-time col-xs-1">
        {times}
      </div>
    );
  }
}

export default connect()(TimesColumn);
