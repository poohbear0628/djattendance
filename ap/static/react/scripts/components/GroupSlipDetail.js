import React, { PropTypes } from 'react'
import { Button, Collapse } from 'react-bootstrap'
import DropdownArrow from './DropdownArrow'
import GroupSlipForm from './GroupSlipForm'
import SelectedEvent from './SelectedEvent'
import { format } from 'date-fns'

import { SLIP_STATUS_LOOKUP, SLIP_TYPE_LOOKUP, FA_ICON_LOOKUP } from '../constants'

const GroupSlipDetail = ({ id, trainees, type, status, TA, trainee, submitted, comments, texted, informed, events, 
                            groupSlipDetailsShow, onClick, removeAllSelectedEvents, removeSelectedEvent, 
                            postGroupSlip, deleteGroupSlip, otherReasonsShow, toggleOtherReasons, 
                            selectedEvents, tas, traineeSelectOptions, traineeId }) => {
  var classes = "row leaveslip-detail " + SLIP_STATUS_LOOKUP[status];

  var faClasses = "fa fa-" + FA_ICON_LOOKUP[SLIP_STATUS_LOOKUP[status]];

  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }
  return (
    <div className={classes}>
      <div className="position-container" onClick={onClick}>
        <i className="fa fa-users" aria-hidden="true"></i>
        <div className="details-container">
          <div>
            <span className="bold">{SLIP_TYPE_LOOKUP[type]} </span>
            <span>{format(submitted, 'MMM D')}</span>
          </div>
          <div className="leaveslip-comments">{comments}</div>
        </div>
        <span className="center-arrow"> 
          <i className={faClasses} aria-hidden="true"></i>
          <DropdownArrow
            directionBoolean={groupSlipDetailsShow[id]}
          />
        </span>
      </div>
      <Collapse in={groupSlipDetailsShow[id]}>
        <div>
          <GroupSlipForm
            post={(groupSlip) => postGroupSlip(groupSlip, selectedEvents, id)}
            deleteGroupSlip={() => deleteGroupSlip(id)}
            submitGroupLeaveSlipShow={true}
            toggleOtherReasons={() => toggleOtherReasons()}
            otherReasonsShow={otherReasonsShow}
            selectedEvents={selectedEvents}
            tas={tas}
            traineeSelectOptions={traineeSelectOptions}
            trainee={trainee}
            traineeId={traineeId}
          />
        </div>
      </Collapse>
    </div>
  )
}

GroupSlipDetail.propTypes = {
  //why do we even need this?!?!?!
}

export default GroupSlipDetail