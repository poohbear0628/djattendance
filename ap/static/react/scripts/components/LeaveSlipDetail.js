import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const LeaveSlipDetail = ({ls, deleteSlip}) => {
  var classes = "row leaveslip-detail " + SLIP_STATUS_LOOKUP[status];
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];
  let slip_status = ''
  if (ls.status === 'P' || ls.status === 'F') {
    slip_status = 'roll__table roll__table--tardy row'
  } else if (ls.status === 'D') {
    slip_status = 'roll__table roll__table--absent row'
  } else {
    slip_status = 'roll__table roll__table--present row'
  }
  return (
    <div className={slip_status} key={ls['id']}> 
      <div className="col-md-6" key={ls['type']}>
        {ls['type']}
      </div>
      <div className="col-md-6">
        <a onClick={() => deleteSlip(ls)}>delete</a>
      </div>
    </div>
  )
}

LeaveSlipDetail.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default LeaveSlipDetail
