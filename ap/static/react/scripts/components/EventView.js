import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { Button, OverlayTrigger, Popover } from 'react-bootstrap'

import { ATTENDANCE_STATUS_LOOKUP, SLIP_STATUS_LOOKUP, FA_ICON_LOOKUP, joinValidClasses } from '../constants'

import { differenceInMinutes, subHours, getHours, getMinutes } from 'date-fns'

//need to refactor so we pass in just event
const EventView = ({ event, roll, slip, gslip, onClick, selectedEvents }) => {
  roll = event.roll;
  slip = event.slip;
  gslip = event.gslip;
  var slipStatus = slip ? slip['status'] : '';
  if (slipStatus == '') {
    slipStatus = gslip ? gslip['status'] : '';
  }
  var rollStatus = roll ? ATTENDANCE_STATUS_LOOKUP[roll['status']] : '';
  var slipClasses = joinValidClasses(['slip', SLIP_STATUS_LOOKUP[slipStatus]]);
  var rollClasses = joinValidClasses([rollStatus, todayClass, 'cal-day__event']);

  if (rollStatus == 'left-class') {
    rollStatus = 'left class';
  }

  var selected = false;
  for (var i = 0; i < selectedEvents.length; i++) {
    if (event.id == selectedEvents[i].id && selectedEvents[i].start_datetime == event.start_datetime) {
      selected = true;
    }
  }

  var todayClass = (event.id === 'TODAY') ? 'today-marker' : '';

  var h = differenceInMinutes(event.end_datetime, event.start_datetime)/3*2
  h = h > 11 ? h : 12

  let datetime = subHours(event.start_datetime, 6)
  let hours = getHours(datetime)*60
  let minutes = getMinutes(datetime)
  var divStyle = {
    top: (hours+minutes)/3*2 + 25,
    height: h,
    opacity: selected ? 0.5 : 1,
  };

  var rollPopover = rollStatus ? 'Roll: ' + rollStatus : '';
  var slipPopover = slipStatus ? 'Slip: ' + SLIP_STATUS_LOOKUP[slipStatus] : '';
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[slipStatus]];

  if (roll && (slip || gslip)) {
    return (
      <OverlayTrigger placement="bottom" overlay={<Popover id={event.id + '-popover'} style={{display: "inline-block"}}>{rollPopover}<br></br> {slipPopover}</Popover>}>
        <div className={rollClasses} style={divStyle} onClick={onClick}>
            {event['code']}
          <div className={slipClasses}><i className={faClasses} aria-hidden="true"></i></div>
        </div>
      </OverlayTrigger>
    )
  }

  if (!roll && (slip || gslip)) {
    return (
      <OverlayTrigger placement="bottom" overlay={<Popover id={event.id + '-popover'} style={{display: "inline-block"}}>{slipPopover}</Popover>}>
        <div className={rollClasses} style={divStyle} onClick={onClick}>
            {event['code']}
          <div className={slipClasses}><i className={faClasses} aria-hidden="true"></i></div>
        </div>
      </OverlayTrigger>
    )
  }

  return (
    <div className={rollClasses} style={divStyle} onClick={onClick}>
        {event['code']}
      <div className={slipClasses}><i className={faClasses} aria-hidden="true"></i></div>
    </div>
  )
}

EventView.propTypes = {
  // event: PropTypes.object.isRequired,
  // roll: PropTypes.object.isRequired,
  // slip: PropTypes.object.isRequired,
  // onClick: PropTypes.func.isRequired
}

export default EventView
