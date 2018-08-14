import React, { Component } from 'react'

import { FA_ICON_LOOKUP } from '../constants'

const SlipStatusIcon = (props) => {
  return (
    <i className={" slip-status fa fa-" + FA_ICON_LOOKUP[props.status]} aria-hidden="true"></i>
  )
}

export default SlipStatusIcon
