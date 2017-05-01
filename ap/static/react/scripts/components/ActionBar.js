import React from 'react'
import PropTypes from 'prop-types'
import { Tabs, Tab, Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'

import SummaryPane from '../containers/SummaryPane'
import RollPane from '../containers/RollPane'
import LeaveSlipPane from '../containers/LeaveSlipPane'
import GroupSlipPane from '../containers/GroupSlipPane'

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
