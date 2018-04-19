import React, { Component } from 'react'
import { format } from 'date-fns'
import { Button } from 'react-bootstrap'

import { ATTENDANCE_MONITOR_GROUP } from '../constants'
import SlipStatusIcon from './SlipStatusIcon'

let dateFormat = 'M/D/YY'
let datetimeFormat = 'M/D/YY h:mm a'

const SlipDetail = ({trainee, slip, deleteSlip, onClick }) => {
  let click = () => onClick(slip)
  let isUnfinalized = '--unfinalized'
  let isAM = trainee.groups.indexOf(ATTENDANCE_MONITOR_GROUP) >= 0
  let isSubmitter = trainee.id == slip.trainee
  return (
  <div className={"row summary__leaveslips-row" + isUnfinalized} onClick={() => click(slip)}>
    <div className="col-xs-2">{format(new Date(slip.submitted), dateFormat)}</div>
    <div className="col-xs-1"><SlipStatusIcon status={slip.status} /></div>
    <div className="col-xs-6">
      {
        slip.classname == 'individual' ? slip.events.map(e =>
          e.name + ' ' + format(moment(e.date), dateFormat)
        ).join(', ') :
        format(new Date(slip.start), datetimeFormat) + ' to ' + format(new Date(slip.end), datetimeFormat)
      }
    </div>
    <div className="col-xs-1">{slip.type.charAt(0).toUpperCase() + slip.type.slice(1).toLowerCase()}</div>
    <div className="col-xs-1 col-xs-offset-1">
      {(isAM || (!slip.finalized && isSubmitter)) &&
        <Button className="summary__leaveslips-button pull-right" bsSize="xsmall" bsStyle="danger"
          onClick={e => {
            if (confirm('Are you sure you want to delete this leave slip?')) {
              deleteSlip(slip)
            }
            e.stopPropagation()
          }}
        >
          <i className="fa fa-close"></i>
        </Button>
      }
    </div>
  </div>
  )
}

export default SlipDetail
