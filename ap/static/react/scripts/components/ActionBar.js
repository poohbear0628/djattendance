import React, { PropTypes } from 'react'
import { Tabs, Tab, Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SummaryPane from '../containers/SummaryPane'
import RollPane from '../containers/RollPane'
import LeaveSlipPane from '../containers/LeaveSlipPane'
import GroupSlipPane from '../containers/GroupSlipPane'

const ActionBar = ({show, isSecondYear, trainee, onSelectTab}) => {
  return (
    <div className="dt">
      <Tabs defaultActiveKey={1} animation={false} id="noanim-tab-example" onSelect={(index) => onSelectTab(index, trainee)}>
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
          <GroupSlipPane />
        </Tab>
      </Tabs>
    </div>
  )
}

ActionBar.propTypes = {
  // submitRoll: PropTypes.bool.isRequired,
  // submitLeaveSlip: PropTypes.bool.isRequired,
  // submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  // selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  // toggleSubmitRoll: PropTypes.func.isRequired,
  // toggleSubmitLeaveSlip: PropTypes.func.isRequired,
  // toggleSubmitGroupSlip: PropTypes.func.isRequired
  // showCalendar: PropTypes.func.isRequired
}

export default ActionBar
