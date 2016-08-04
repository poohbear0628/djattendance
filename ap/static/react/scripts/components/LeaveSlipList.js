import React, { PropTypes } from 'react'
import { Collapse } from 'react-bootstrap'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail from './GroupSlipDetail'
import DropdownArrow from './DropdownArrow'

const LeaveSlipList = ({ slips, gslips, leaveSlipsShow, leaveSlipDetailsShow, groupSlipDetailsShow,
                          toggleLeaveSlipDetail, toggleGroupSlipDetail, removeAllSelectedEvents, removeSelectedEvent, 
                          postRollSlip, deleteSlip, postGroupSlip, deleteGroupSlip, otherReasonsShow, toggleLeaveSlips, toggleOtherReasons, 
                          selectedEvents, tas, traineeSelectOptions, traineeId }) => {
  return (
    <div className="toggle-title details-container leaveslips">
      <span onClick={toggleLeaveSlips}>
        <span className="toggle-title-text">Leave Slip History</span>
        <DropdownArrow
          directionBoolean={true}
        />
      </span>
      <Collapse in={false}>
        <div>
          <div className="toggle-title-mid">
            <span>
              Pending ({slips.pending.length + gslips.pending.length})
            </span>
            <div>
              {slips.pending.map(function(slip) {
                return <LeaveSlipDetail
                          {...slip}
                          leaveSlipDetailsShow={leaveSlipDetailsShow}
                          onClick={() => toggleLeaveSlipDetail(slip.id, slip.events, slip.type, slip.TA, slip.comments, slip.informed)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postRollSlip={(rollSlip, selectedEvents, slipId) => postRollSlip(rollSlip, selectedEvents, slipId)}
                          deleteSlip={(slipId) => deleteSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                        />
              })}
              {gslips.pending.map(function(gslip) {
                return <GroupSlipDetail
                          {...gslip}
                          groupSlipDetailsShow={groupSlipDetailsShow}
                          onClick={() => toggleGroupSlipDetail(gslip.id, gslip.start, gslip.end, gslip.type, gslip.TA, gslip.comments, gslip.informed, gslip.trainees)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postGroupSlip={(groupSlip, selectedEvents, slipId) => postGroupSlip(groupSlip, selectedEvents, slipId)}
                          deleteGroupSlip={(slipId) => deleteGroupSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                          traineeSelectOptions={traineeSelectOptions}
                          traineeId={traineeId}
                        />
              })}
            </div>
          </div>
          <div className="toggle-title-mid">
            <span>
              Denied ({slips.denied.length + gslips.denied.length})
            </span>
            <div>
              {slips.denied.map(function(slip) {
                return <LeaveSlipDetail
                          {...slip}
                          leaveSlipDetailsShow={leaveSlipDetailsShow}
                          onClick={() => toggleLeaveSlipDetail(slip.id, slip.events, slip.type, tas[slip.TA], slip.comments, slip.informed)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postRollSlip={(rollSlip, selectedEvents, slipId) => postRollSlip(rollSlip, selectedEvents, slipId)}
                          deleteSlip={(slipId) => deleteSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                        />
              })}
              {gslips.denied.map(function(gslip) {
                return <GroupSlipDetail
                          {...gslip}
                          groupSlipDetailsShow={groupSlipDetailsShow}
                          onClick={() => toggleGroupSlipDetail(gslip.id, gslip.start, gslip.end, gslip.type, gslip.TA, gslip.comments, gslip.informed, gslip.trainees)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postGroupSlip={(groupSlip, selectedEvents, slipId) => postGroupSlip(groupSlip, selectedEvents, slipId)}
                          deleteGroupSlip={(slipId) => deleteGroupSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                          traineeSelectOptions={traineeSelectOptions}
                          traineeId={traineeId}
                        />
              })}
            </div>
          </div>
          <div className="toggle-title-mid">
            <span>
              Approved ({slips.approved.length + gslips.approved.length})
            </span>
            <div>
              {slips.approved.map(function(slip) {
                return <LeaveSlipDetail
                          {...slip}
                          leaveSlipDetailsShow={leaveSlipDetailsShow}
                          onClick={() => toggleLeaveSlipDetail(slip.id, slip.events, slip.type, tas[slip.TA], slip.comments, slip.informed)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postRollSlip={(rollSlip, selectedEvents, slipId) => postRollSlip(rollSlip, selectedEvents, slipId)}
                          deleteSlip={(slipId) => deleteSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                        />
              })}
              {gslips.approved.map(function(gslip) {
                return <GroupSlipDetail
                          {...gslip}
                          groupSlipDetailsShow={groupSlipDetailsShow}
                          onClick={() => toggleGroupSlipDetail(gslip.id, gslip.start, gslip.end, gslip.type, gslip.TA, gslip.comments, gslip.informed, gslip.trainees)}
                          removeAllSelectedEvents={() => removeAllSelectedEvents()}
                          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
                          postGroupSlip={(groupSlip, selectedEvents, slipId) => postGroupSlip(groupSlip, selectedEvents, slipId)}
                          deleteGroupSlip={(slipId) => deleteGroupSlip(slipId)}
                          toggleOtherReasons={() => toggleOtherReasons()}
                          otherReasonsShow={otherReasonsShow}
                          selectedEvents={selectedEvents}
                          tas={tas}
                          traineeSelectOptions={traineeSelectOptions}
                          traineeId={traineeId}
                        />
              })}
            </div>
          </div>
        </div>
      </Collapse>
    </div>
  )
}

LeaveSlipList.propTypes = {
  slips: PropTypes.object.isRequired
}

export default LeaveSlipList