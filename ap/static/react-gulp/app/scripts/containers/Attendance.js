import React, { Component, PropTypes } from 'react'

import Trainee from '../components/Trainee'
import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import DaysContainer from '../containers/DaysContainer'
import TimesColumn from '../components/TimesColumn'
import AttendanceBar from '../containers/AttendanceBar'
import AttendanceActions from '../containers/AttendanceActions'

const Attendance = () => (
  <div className="container">
    <WeekNav />
    <div className="row">
      <div className="col-md-8">
        <AttendanceActions />
        <AttendanceBar />
      </div>
      <div className="col-md-16 event-grid">
        <TimesColumn />
        <GridContainer />
      </div>
    </div>
  </div>
)

export default Attendance