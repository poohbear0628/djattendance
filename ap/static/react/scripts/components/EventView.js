import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Button, OverlayTrigger, Popover } from 'react-bootstrap'

import { ATTENDANCE_STATUS_LOOKUP, SLIP_STATUS_LOOKUP, FA_ICON_LOOKUP, joinValidClasses } from '../constants'

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
<<<<<<< HEAD

=======
  
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  var slipClasses = joinValidClasses(['slip', SLIP_STATUS_LOOKUP[slipStatus]]);
  var rollClasses = joinValidClasses([rollStatus, todayClass, 'cal-day__event']);

  if (rollStatus == 'left-class') {
    rollStatus = 'left class';
  }

  var selected = false;
  for (var i = 0; i < selectedEvents.length; i++) {
    if (event.id == selectedEvents[i].id && selectedEvents[i].start == event.start) {
      selected = true;
    }
  }

  var todayClass = (event.id === 'TODAY') ? 'today-marker' : '';

  var h = dateFns.differenceInMinutes(event['end'], event['start'])/3*2
  h = h > 11 ? h : 12

  let datetime = dateFns.subHours(event['start'], 6)
  let hours = dateFns.getHours(datetime)*60
  let minutes = dateFns.getMinutes(datetime)
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
<<<<<<< HEAD
      <OverlayTrigger placement="bottom" overlay={<Popover id={event.id + '-popover'} style={{display: "inline-block"}}>{rollPopover}<br></br> {slipPopover}</Popover>}>
=======
      <OverlayTrigger placement="bottom" overlay={<Popover style={{display: "inline-block"}}>{rollPopover}<br></br> {slipPopover}</Popover>}>
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
        <div className={rollClasses} style={divStyle} onClick={onClick}>
            {event['code']}
          <div className={slipClasses}><i className={faClasses} aria-hidden="true"></i></div>
        </div>
      </OverlayTrigger>
    )
  }

  if (!roll && (slip || gslip)) {
    return (
<<<<<<< HEAD
      <OverlayTrigger placement="bottom" overlay={<Popover id={event.id + '-popover'} style={{display: "inline-block"}}>{slipPopover}</Popover>}>
=======
      <OverlayTrigger placement="bottom" overlay={<Popover style={{display: "inline-block"}}>{slipPopover}</Popover>}>
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
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
