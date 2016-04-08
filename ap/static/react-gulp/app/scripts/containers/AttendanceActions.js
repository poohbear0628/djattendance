import { connect } from 'react-redux'
import { toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip,
          toggleLeaveSlips, toggleOtherReasons,
          removeSelectedEvent, removeAllSelectedEvents } from '../actions'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  return {
    submitRollShow: state.submitRollShow,
    submitLeaveSlipShow: state.submitLeaveSlipShow,
    submitGroupLeaveSlipShow: state.submitGroupLeaveSlipShow,
    otherReasonsShow: state.otherReasonsShow,
    selectedEvents: state.selectedEvents
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