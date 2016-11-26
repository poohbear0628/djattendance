import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const LeaveSlipDetail = ({ls, deleteSlip}) => {
  console.log(ls, 'leaveslipdetail');
  var status = ls['status'];
  var classes = "row leaveslip-detail " + SLIP_STATUS_LOOKUP[status];
  console.log(classes);
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];
  console.log(faClasses);

  
  return (
    <tr className='roll__table--tardy' key={ls['id']}> 
      <td>
        {ls['type']}
      </td>
      <td>
        {SLIP_STATUS_LOOKUP[status]}
      </td>
      <td>
        <a onClick={() => deleteSlip(ls)}>edit</a> | <a onClick={() => deleteSlip(ls)}>delete</a>
      </td>
    </tr>
  )
}

LeaveSlipDetail.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default LeaveSlipDetail