import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Button, Collapse } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipList from './LeaveSlipList'
import DropdownArrow from './DropdownArrow'

const AttendanceDetails = ({ unexcusedAbsences, unexcusedTardies, excused, slips, selectedEvents, tas,
                              unexcusedAbsencesShow, unexcusedTardiesShow, excusedShow, leaveSlipsShow, leaveSlipDetailsShow, otherReasonsShow,
                              onAbsencesToggle, onTardiesToggle, onExcusedToggle, toggleLeaveSlips, toggleLeaveSlipDetail, toggleOtherReasons,
                              removeAllSelectedEvents, removeSelectedEvent, postRollSlip, deleteSlip }) => {

  return (
    <div style={{margin: "15px 0px 40px 10px"}}>
      <div className="toggle-title">
        <span onClick={onAbsencesToggle}>
          Unexcused Absences ({unexcusedAbsences.length})
        </span>
        <DropdownArrow
          directionBoolean={unexcusedAbsencesShow}
        />
        <Collapse in={unexcusedAbsencesShow}>
          <div>
            {unexcusedAbsences.map(ua =>
              <RollDetail
                {...ua}
              />
            )}
          </div>
        </Collapse>
      </div>
      <div className="toggle-title">
        <span onClick={onTardiesToggle}>
          Unexcused Tardies ({unexcusedTardies.length})
        </span>
        <DropdownArrow
          directionBoolean={unexcusedTardiesShow}
        />
        <Collapse in={unexcusedTardiesShow}>
          <div>
            {unexcusedTardies.map(ut =>
              <RollDetail
                {...ut}
              />
            )}
          </div>
        </Collapse>
      </div>
      <div className="toggle-title">
        <span onClick={onExcusedToggle}>
          Excused ({excused.length})
        </span>
        <DropdownArrow
          directionBoolean={excusedShow}
        />
        <Collapse in={excusedShow}>
          <div>
            {excused.map(e =>
              <RollDetail
                {...e}
              />
            )}
          </div>
        </Collapse>
      </div>
      <div className="toggle-title">
        <span onClick={toggleLeaveSlips}>
          Leave Slip History
        </span>
        <DropdownArrow
          directionBoolean={leaveSlipsShow}
        />
        <LeaveSlipList
          slips={slips}
          leaveSlipsShow={leaveSlipsShow}
          leaveSlipDetailsShow={leaveSlipDetailsShow}
          onDetailClick={(id, evs, slipType, TA, comments, informed) => toggleLeaveSlipDetail(id, evs, slipType, TA, comments, informed)}
          otherReasonsShow={otherReasonsShow}
          toggleOtherReasons={() => toggleOtherReasons()}
          selectedEvents={selectedEvents}
          tas={tas}
          removeAllSelectedEvents={() => removeAllSelectedEvents()}
          removeSelectedEvent={(ev) => removeSelectedEvent(ev)}
          postRollSlip={(rollSlip, selectedEvents, slipId) => postRollSlip(rollSlip, selectedEvents, slipId)}
          deleteSlip={(slipId) => deleteSlip(slipId)}
        />
      </div>
    </div>
  )
}

AttendanceDetails.propTypes = {
  unexcusedAbsences: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  unexcusedAbsencesShow: PropTypes.bool.isRequired,
  unexcusedTardiesShow: PropTypes.bool.isRequired,
  excusedShow: PropTypes.bool.isRequired,
  onAbsencesToggle: PropTypes.func.isRequired,
  onTardiesToggle: PropTypes.func.isRequired,
  onExcusedToggle: PropTypes.func.isRequired
};

export default AttendanceDetails