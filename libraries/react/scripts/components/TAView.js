import React, { Component } from 'react'
import PropTypes from 'prop-types'

import TAActions from '../containers/TAActions'
import Calendar from '../components/Calendar'

const TAView = () => (
    <div className="attendance container-fluid">
      <div className="row">
        <div className="col-md-5">
          <TAActions />
        </div>
        <div className="col-md-7 cal">
          <Calendar />
        </div>
      </div>
    </div>
)

export default TAView
