import { connect } from 'react-redux'
import { postRollSlip, deleteLeaveSlip, postGroupSlip,
          deselectEvent, deselectAllEvents } from '../actions'
import { getEventsByRollStatus } from '../selectors/selectors'
import { sortEsr, sortSlips } from '../constants'
import DetailsBar from '../components/DetailsBar'


const mapStateToProps = (state) => {
  return {
    esr: getEventsByRollStatus(state)
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    postRollSlip: (rollSlip, selectedEvents, slipId) => {
      dispatch(postRollSlip(rollSlip, selectedEvents, slipId))
    },
    deleteSlip: (slipId) => {
      dispatch(deleteLeaveSlip(slipId))
    },
    postGroupSlip: (groupSlip, selectedEvents) => {
      dispatch(postGroupSlip(groupSlip, selectedEvents))
    },
    onAbsencesToggle: () => {
      dispatch(toggleUnexcusedAbsences())
    },
    onTardiesToggle: () => {
      dispatch(toggleUnexcusedTardies())
    },
    onExcusedToggle: () => {
      dispatch(toggleExcused())
    },
    removeAllSelectedEvents: () => {
      dispatch(deselectAllEvents())
    },
    removeSelectedEvent: (ev) => {
      dispatch(deselectEvent(ev))
    }
  }
}

const AttendanceDetails = connect(
  mapStateToProps,
  mapDispatchToProps
)(DetailsBar)

export default AttendanceDetails