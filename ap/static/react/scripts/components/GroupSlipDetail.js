import React from 'react'
import { Button, Collapse } from 'react-bootstrap'
import { format } from 'date-fns'
import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const GroupSlipDetail = ({gls, deleteSlip}) => {
  console.log(gls, 'groupslipdetail');
  var status = gls['status'];
  var classes = "row groupslip-detail " + SLIP_STATUS_LOOKUP[status];
  console.log(classes);
  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];
  console.log(faClasses);

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
  )
}

GroupSlipDetail.propTypes = {
  //TODO: we should add these AFTER the dust settles
}

export default GroupSlipDetail
