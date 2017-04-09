import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const GroupSlipDetail = ({gls, deleteSlip}) => {
  console.log(gls, 'groupslipdetail');
  var status = gls['status'];
  var classes = "row groupslip-detail " + SLIP_STATUS_LOOKUP[status];
  console.log(classes);
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];
  console.log(faClasses);


  return (
    <tr className='roll__table--tardy' key={gls['id']}>
      <td>
        {gls['type']}
      </td>
      <td>
        {SLIP_STATUS_LOOKUP[status]}
      </td>
    </tr>
  )
}

GroupSlipDetail.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default GroupSlipDetail
