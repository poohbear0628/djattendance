import React from 'react'
import PropTypes from 'prop-types'

import RollPane from '../containers/RollPane'
import LeaveSlipPane from '../containers/LeaveSlipPane'
import GroupSlipPane from '../containers/GroupSlipPane'
import TraineeSelectorContainer from '../containers/TraineeSelectorContainer'
import { ATTENDANCE_MONITOR_GROUP } from '../constants'

const TABar = ({show, trainee, traineeView}) => {
	var display = null;
	if (show == 'roll') {
		display = <RollPane />
	} else if (show == 'leaveslip') {
		display = <LeaveSlipPane />
	} else if (show == 'groupslip') {
		display = <GroupSlipPane />
	}
  return (
    <div className="dt">
      <h2 className="dt__actionbar-heading">TA {show.charAt(0).toUpperCase() + show.slice(1)} View</h2>
      {display}
    </div>
  )
}

TABar.propTypes = {
  // submitRoll: PropTypes.bool.isRequired,
  // submitLeaveSlip: PropTypes.bool.isRequired,
  // submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  // selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  // toggleSubmitRoll: PropTypes.func.isRequired,
  // toggleSubmitLeaveSlip: PropTypes.func.isRequired,
  // toggleSubmitGroupSlip: PropTypes.func.isRequired
  // showCalendar: PropTypes.func.isRequired
}

export default TABar
