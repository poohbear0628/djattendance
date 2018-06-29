import React, { Component } from 'react'
import PropTypes from 'prop-types'

import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import AttendanceActions from '../containers/AttendanceActions'
import Calendar from '../components/Calendar'

const Attendance = () => (
    <div className="attendance container-fluid">
      <div className="row">
        <div className="col-md-5">
          <AttendanceActions />
        </div>
        <div className="col-md-7 cal">
          <Calendar />
        </div>
      </div>
    </div>
)

export default Attendance
