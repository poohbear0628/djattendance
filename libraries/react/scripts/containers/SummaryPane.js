import { connect } from 'react-redux'
import { deleteLeaveSlip, editLeaveSlip, editGroupLeaveSlip } from '../actions'
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
    deleteSlip: (slip) => {
      dispatch(deleteLeaveSlip(slip))
    },
    editSlip: (slip) => {
      dispatch(editLeaveSlip(slip))
    },
    editGroupSlip: (slip) => {
      dispatch(editGroupLeaveSlip(slip))
    },
  }
}

const SummaryPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(Summary)

export default SummaryPane
