import React, { PropTypes } from 'react'
import { Tabs, Tab, Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SummaryPane from '../containers/SummaryPane'
import RollPane from '../containers/RollPane'
import LeaveSlipPane from '../containers/LeaveSlipPane'
import GroupSlipPane from '../containers/GroupSlipPane'

<<<<<<< HEAD
const ActionBar = ({show, trainee, onSelectTab}) => {
  return (
    <div className="dt">
      <Tabs activeKey={["summary", "roll", "leaveslip", "groupslip"].indexOf(show)} animation={false} id="noanim-tab-example" onSelect={onSelectTab}>
        <Tab eventKey={0} title="Summary">
          <SummaryPane />
        </Tab>
        {trainee.self_attendance ?
          <Tab eventKey={1} title="Roll">
            <RollPane />
          </Tab>
          : '' }
        <Tab eventKey={2} title="Leave Slips">
          <LeaveSlipPane />
        </Tab>
        <Tab eventKey={3} title="Group Slips">
=======
const ActionBar = ({show, onShowCalendar, isSecondYear, showRoll, showSummary, showLeaveslip, showGroupslip}) => {
  return (
    <div className="dt">
      <Tabs defaultActiveKey={1} animation={false} id="noanim-tab-example" onSelect={(index) => onShowCalendar(index, show)}>
        <Tab eventKey={1} title="Summary">
          <SummaryPane />
        </Tab>
        {isSecondYear ? 
          <Tab eventKey={2} title="Roll">
            <RollPane />
          </Tab>
          : '' }
        <Tab eventKey={3} title="LeaveSlip">
          <LeaveSlipPane />
        </Tab>
        <Tab eventKey={4} title="GroupSlip">
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
          <GroupSlipPane />
        </Tab>
      </Tabs>
    </div>
  )
}

ActionBar.propTypes = {
<<<<<<< HEAD
  // submitRoll: PropTypes.bool.isRequired,
  // submitLeaveSlip: PropTypes.bool.isRequired,
  // submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  // selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  // toggleSubmitRoll: PropTypes.func.isRequired,
  // toggleSubmitLeaveSlip: PropTypes.func.isRequired,
=======
  // submitRoll: PropTypes.bool.isRequired, 
  // submitLeaveSlip: PropTypes.bool.isRequired, 
  // submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  // selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  // toggleSubmitRoll: PropTypes.func.isRequired, 
  // toggleSubmitLeaveSlip: PropTypes.func.isRequired, 
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  // toggleSubmitGroupSlip: PropTypes.func.isRequired
  // showCalendar: PropTypes.func.isRequired
}

export default ActionBar
