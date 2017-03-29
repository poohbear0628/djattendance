import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Button, Collapse } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipList from './LeaveSlipList'
import DropdownArrow from './DropdownArrow'

const AttendanceDetails = ({ unexcusedAbsences, unexcusedTardies, excused, selectedEvents,
                              unexcusedAbsencesShow, unexcusedTardiesShow, excusedShow,
                              onAbsencesToggle, onTardiesToggle, onExcusedToggle }) => {

  return (
    <div className="details-container attendance">
      <div className="toggle-title">
          <span className="toggle-title-text">Unexcused Absences</span>
          <DropdownArrow
            directionBoolean={true}
          />
      </div>
    </div>
  )
}

AttendanceDetails.propTypes = {
  // unexcusedAbsences: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  // unexcusedAbsencesShow: PropTypes.bool.isRequired,
  // unexcusedTardiesShow: PropTypes.bool.isRequired,
  // excusedShow: PropTypes.bool.isRequired,
  // onAbsencesToggle: PropTypes.func.isRequired,
  // onTardiesToggle: PropTypes.func.isRequired,
  // onExcusedToggle: PropTypes.func.isRequired
};

export default AttendanceDetails