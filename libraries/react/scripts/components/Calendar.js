import React, { Component } from 'react'
import PropTypes from 'prop-types'

import WeekNav from '../containers/WeekNav'
import GridContainer from '../containers/GridContainer'
import AttendanceActions from '../containers/AttendanceActions'

const Calendar = () => (
  <div>
    <div className="row">
      <WeekNav />
    </div>
    <div className="row">
      <GridContainer />
    </div>
  </div>
)

export default Calendar
