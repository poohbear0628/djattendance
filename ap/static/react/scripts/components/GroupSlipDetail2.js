import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const GroupSlipDetail2 = ({gls, deleteSlip}) => {
<<<<<<< HEAD
  let slip_status = ''
  if (gls.status === 'P' || gls.status === 'F') {
    slip_status = 'roll__table roll__table--tardy row'
  } else if (gls.status === 'D') {
    slip_status = 'roll__table roll__table--absent row'
  } else {
    slip_status = 'roll__table roll__table--present row'
  }
  return (
    <div className={slip_status} key={gls['id']}> 
      <div className="col-md-4" key={gls['type']}>
        {gls['type']}
      </div>
      <div className="col-md-4">
        {gls['comments']}
      </div>
      <div className="col-md-4">
        {gls['trainees_names']}
      </div>
    </div>
=======
  console.log(gls, 'groupslipdetail2');
  var status = gls['status'];
  var classes = "row groupslip-detail2 " + SLIP_STATUS_LOOKUP[status];
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
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  )
}

GroupSlipDetail2.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default GroupSlipDetail2