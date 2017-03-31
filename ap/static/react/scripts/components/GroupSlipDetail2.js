import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const GroupSlipDetail2 = ({gls, deleteSlip, deleteGroupSlip}) => {
  console.log(gls, 'groupslipdetail2');
  var status = gls['status'];
  var classes = "row groupslip-detail2 " + SLIP_STATUS_LOOKUP[status];
  console.log(classes);
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];
  console.log(faClasses);

  
  return (
    <tr className='roll__table--tardy' key={gls['id']}>
      <a href={"/leaveslips/group/update/"+gls['id']}>
      <td>
        {gls['type']}
      </td>
      </a>
      <td>
        {SLIP_STATUS_LOOKUP[status]}
      </td>
      <td>
        <a href={"/leaveslips/group/update/"+gls['id']}>update</a> &nbsp;
        <a onClick={() => deleteGroupSlip(gls)}>delete</a>
      </td>
    </tr>
  )
}

GroupSlipDetail2.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default GroupSlipDetail2