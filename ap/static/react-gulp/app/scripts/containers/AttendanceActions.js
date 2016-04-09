import { connect } from 'react-redux'
import { toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip,
          toggleLeaveSlips, toggleOtherReasons,
          removeSelectedEvent, removeAllSelectedEvents } from '../actions'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  console.log(state);
  return {
    submitRollShow: state.reducer.submitRollShow,
    submitLeaveSlipShow: state.reducer.submitLeaveSlipShow,
    submitGroupLeaveSlipShow: state.reducer.submitGroupLeaveSlipShow,
    otherReasonsShow: state.reducer.otherReasonsShow,
    selectedEvents: state.reducer.selectedEvents
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    toggleSubmitRoll: () => {
      dispatch(toggleSubmitRoll())
    },
    toggleSubmitLeaveSlip: () => {
      dispatch(toggleSubmitLeaveSlip())
    },
    toggleSubmitGroupLeaveSlip: () => {
      dispatch(toggleSubmitGroupLeaveSlip())
    },
    toggleOtherReasons: () => {
      dispatch(toggleOtherReasons())
    },
    removeSelectedEvent: (ev) => {
      dispatch(removeSelectedEvent(ev))
    },
    removeAllSelectedEvents: () => {
      dispatch(removeAllSelectedEvents())
    }
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions