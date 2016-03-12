import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { nextWeek, prevWeek, toggleEvent, setRollStatus } from '../actions'
import trainee from '../testdata/trainee'
import rolls from '../testdata/rolls'
import events from '../testdata/events'
import slips from '../testdata/slips'
import Trainee from '../components/Trainee'
import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import DaysContainer from '../containers/DaysContainer'
import TimesColumn from '../components/TimesColumn'
import AttendanceBar from '../containers/AttendanceBar'

import { joinValidClasses } from '../constants'

const Attendance = () => (
  <div className="container">
    <WeekNav />
    <div className="row">
      <div className="col-md-4 col-xs-4"></div>
      <DaysContainer />
    </div>
    <div className="row">
      <div className="col-md-4">
        <AttendanceBar />
      </div>
      {/*<DaysContainer />*/}
      <TimesColumn />
      <GridContainer />
    </div>
  </div>
)

export default Attendance