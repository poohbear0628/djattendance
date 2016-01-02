import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { ATTENDANCE_STATUS_LOOKUP, SLIP_STATUS_LOOKUP, ROLL_CODE_LOOKUP, joinValidClasses } from '../constants'

class EventView extends Component {
  render() {
    var ev = this.props.event;

    console.log("event", event);

    var rolls = this.props.rolls;
    console.log("rolls", rolls);

    var i = 0;
    while (i < rolls.length) {
      if (rolls[i].event == ev.id) {
        console.log("roll", rolls[i]);
        break;
      }
      i++;
    }

    console.log("roll", rolls[i]);
    var roll = rolls[i];

    var status = roll ? ATTENDANCE_STATUS_LOOKUP[roll['status']] : '';
    var todayClass = (ev.id === 'TODAY') ? 'today-marker' : '';

    var slips = this.props.slips;
    var i = 0;
    while (i < slips.length) {
      if (slips[i].events[0] == ev.id) { //this is broken!!!!
        break;
      }
      i++;
    }

    var leaveslip = slips[i]
    var slipStatus = leaveslip ? leaveslip['status'] : '';
    var rollClasses = joinValidClasses([status, todayClass, 'schedule-event']); //ev['selected']
    var slipClasses = joinValidClasses(['slip', SLIP_STATUS_LOOKUP[slipStatus]]);
    // ev['rolls').at(ev['rolls').length - 1)['roll')
    var divStyle = {
      top: moment.duration(moment(ev['start']).format('H:m')).subtract(6, 'hours').asMinutes()/3*2,
      height: moment(ev['end']).diff(moment(ev['start']), 'minutes')/3*2,
    };
    return(
      <div className={rollClasses} onClick={this.toggleEvent} style={divStyle}>
        {ROLL_CODE_LOOKUP[ev['code']]}
        <div className={slipClasses}>{slipStatus}</div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    slips: state.slips,
    rolls: state.rolls
  };
}

export default connect(mapStateToProps)(EventView);