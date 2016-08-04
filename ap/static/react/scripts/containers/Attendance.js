import React, { Component, PropTypes } from 'react'

import Trainee from '../components/Trainee'
import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import AttendanceDetails from '../containers/AttendanceDetails'
import AttendanceActions from '../containers/AttendanceActions'
import SlipDetails from '../containers/SlipDetails'

const Attendance = () => (
  <div className="attendance">
    <WeekNav />
    <div className="row">
      <div className="col-md-4">
        <AttendanceActions />
        <AttendanceDetails />
        <SlipDetails />
      </div>
      <div className="col-md-8 cal">
        <GridContainer />
      </div>
    </div>
  </div>
)

export default Attendance