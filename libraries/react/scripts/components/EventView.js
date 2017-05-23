import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { Button, OverlayTrigger, Popover } from 'react-bootstrap'

import { ATTENDANCE_STATUS_LOOKUP, SLIP_STATUS_LOOKUP, FA_ICON_LOOKUP, joinValidClasses } from '../constants'

import { differenceInMinutes, subHours, getHours, getMinutes } from 'date-fns'

const EventView = ({ event, status, onClick, selected }) => {
  var todayClass = (event.id === 'TODAY') ? 'today-marker' : '';

  const START_TIME = 6
  const PIXELS_PER_MINUTE = 2/3
  let datetime = subHours(event.start_datetime, START_TIME)
  let minutes = getMinutes(datetime) + getHours(datetime)*60
  var divStyle = {
    top: minutes * PIXELS_PER_MINUTE + 25,
    height: Math.max(differenceInMinutes(event.end_datetime, event.start_datetime) * PIXELS_PER_MINUTE, 12),
    opacity: selected ? 0.5 : 1,
  };

  // replace "-" in css class e.g. left-class with human-friendly " "
  let roll = event.roll
  var rollStatus = (roll ? ATTENDANCE_STATUS_LOOKUP[roll.status] : '').replace('-', ' ')
  var rollPopover = rollStatus ? 'Roll: ' + rollStatus : '';
  var slipPopover = status.slip ? 'Slip: ' + status.slip : '';
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[status.slip]
  var rollClasses = joinValidClasses([status.roll, todayClass, 'cal-day__event'])

  let eventView = (
    <div className={rollClasses} style={divStyle} onClick={onClick}>
      {event.code}
      <div className={joinValidClasses(['slip', status.slip])}><i className={faClasses} aria-hidden="true"></i></div>
    </div>
  )
  if (roll || status.slip) {
    return (
      <OverlayTrigger overlay={
        <Popover id={event.id + '-popover'}>
          {rollPopover}
          {rollPopover ? <br></br> : ''}
          {slipPopover}
        </Popover>
        }>
        {eventView}
      </OverlayTrigger>
    )
  }
  else {
    return eventView
  }
}

EventView.propTypes = {
  // event: PropTypes.object.isRequired,
  // roll: PropTypes.object.isRequired,
  // slip: PropTypes.object.isRequired,
  // onClick: PropTypes.func.isRequired
}

export default EventView
