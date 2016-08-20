import { connect } from 'react-redux'
import { selectLeaveslip, selectGroupslip, selectEvent } from '../actions'
import { getGroupSlipsforPeriod, getLeaveSlipsforPeriod, getEventsByRollStatus } from '../selectors/selectors'
import Summary from '../components/Summary'

const mapStateToProps = (state) => {
  return {    
    eventsRolls: getEventsByRollStatus(state),
    groupslips: getGroupSlipsforPeriod(state),
    leaveslips: getLeaveSlipsforPeriod(state),
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    selectLeaveslip,
    selectGroupslip,
    selectEvent,
  }
}

const SummaryPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(Summary)

export default SummaryPane