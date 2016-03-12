import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Button, OverlayTrigger, Popover } from 'react-bootstrap'

import { ATTENDANCE_STATUS_LOOKUP, SLIP_STATUS_LOOKUP, ROLL_CODE_LOOKUP, joinValidClasses } from '../constants'

const EventView = ({ event, roll, slip }) => {
  var slipStatus = slip ? slip['status'] : '';
  var rollStatus = roll ? ATTENDANCE_STATUS_LOOKUP[roll['status']] : '';

  var slipClasses = joinValidClasses(['slip', SLIP_STATUS_LOOKUP[slipStatus]]);
  var rollClasses = joinValidClasses([rollStatus, todayClass, 'schedule-event', 'col-md-1', 'col-xs-1']); //event['selected']
  var todayClass = (event.id === 'TODAY') ? 'today-marker' : '';

  var divStyle = {
    top: moment.duration(moment(event['start']).format('H:m')).subtract(6, 'hours').asMinutes()/3*2,
    height: moment(event['end']).diff(moment(event['start']), 'minutes')/3*2,
  };

  var rollPopover = rollStatus ? 'Roll: ' + rollStatus : '';
  var slipPopover = slipStatus ? 'Leave Slip: ' + SLIP_STATUS_LOOKUP[slipStatus] : '';

  return (
    <OverlayTrigger trigger="hover" placement="bottom" overlay={<Popover style={{width: 160}}>{rollPopover}<br></br> {slipPopover}</Popover>}>
      <div className={rollClasses} style={divStyle}>
          {ROLL_CODE_LOOKUP[event['code']]}
        <div className={slipClasses}>{slipStatus}</div>
      </div>
    </OverlayTrigger>
  )
}

EventView.propTypes = {
  event: PropTypes.object.isRequired,
  roll: PropTypes.object.isRequired,
  slip: PropTypes.object.isRequired
}

export default EventView
