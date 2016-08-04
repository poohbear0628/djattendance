import React, { PropTypes } from 'react'
import { Tabs, Tab, Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SelectedEvent from './SelectedEvent'
import RollSlipForm from './RollSlipForm'
import GroupSlipForm from './GroupSlipForm'

const ActionBar = ({toggle,
                    selectedEvents, formSuccess, trainee, traineeSelectOptions, isSecondYear, tas, lsdShow, gsdShow, otherReasonsShow,
                    toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupSlip, toggleOtherReasons,
                    removeSelectedEvent, removeAllSelectedEvents, postRollSlip, postGroupSlip }) => {
  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }

  var hideRoll = {};
  if (trainee.terms_attended[trainee.terms_attended.length-1] <= 2) {
    hideRoll = {display: "none"};
  }

  return (
    <div className="dt">
      <Tabs defaultActiveKey={1} animation={false} id="noanim-tab-example">
        <Tab eventKey={1} title="Summary">Tab 1 content</Tab>
        <Tab eventKey={2} title="Roll">Tab 2 content</Tab>
        <Tab eventKey={3} title="LeaveSlip">Tab 2 content</Tab>
        <Tab eventKey={4} title="GroupSlip">Tab 3 content</Tab>
      </Tabs>
    </div>
  )
}

ActionBar.propTypes = {
  // submitRoll: PropTypes.bool.isRequired, 
  // submitLeaveSlip: PropTypes.bool.isRequired, 
  // submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  toggleSubmitRoll: PropTypes.func.isRequired, 
  toggleSubmitLeaveSlip: PropTypes.func.isRequired, 
  toggleSubmitGroupSlip: PropTypes.func.isRequired
}

export default ActionBar
