import React, { Component, PropTypes } from 'react'

import Trainee from '../components/Trainee'
import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import AttendanceDetails from '../containers/AttendanceDetails'
import AttendanceActions from '../containers/AttendanceActions'

const Attendance = () => (
    <div className="attendance container">
      <div className="row">
        <div className="col-md-6">
          <AttendanceActions />
        </div>
        <div className="col-md-6 cal">
          <div className="row">
            <WeekNav />
          </div>
          <div className="row">
            <GridContainer />
          </div>
        </div>
      </div>
    </div>
)

export default Attendance
