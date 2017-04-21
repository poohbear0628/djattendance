import { connect } from 'react-redux'
import { selectLeaveslip, selectGroupslip, selectEvent, deleteLeaveSlip } from '../actions'
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
    deleteSlip: (slip) => {
      dispatch(deleteLeaveSlip(slip))
    },
<<<<<<< HEAD
    editSlip: (slip) => {
      dispatch(postLeaveSlip(slip))
    }
=======
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  }
}

const SummaryPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(Summary)

export default SummaryPane