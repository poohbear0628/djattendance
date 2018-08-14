import React from 'react'
import { SLIP_STATUS_DISPLAY } from '../constants'

const TALabels = (slip) => {
  return (
  	<div className="dt-leaveslip__labels">
      {slip.status == 'S' && <span className="label label-info">{SLIP_STATUS_DISPLAY[slip.status]}</span>}
      {slip.status == 'F' && <span className="label label-warning">{SLIP_STATUS_DISPLAY[slip.status]}</span>}
      {slip.texted && <span className="label label-primary">Texted Attendance Number</span>}
      {slip.informed && <span className="label label-default">Informed TA</span>}
      {slip.late && <span className="label label-danger">Submitted Late</span>}
  	</div>
  )
}

export default TALabels
