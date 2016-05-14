import { connect } from 'react-redux'
import { toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip,
          toggleLeaveSlips, toggleOtherReasons, removeSelectedEvent, removeAllSelectedEvents,
          postRollSlip, postGroupLeaveSlip } from '../actions'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  var ta_names = [];
  for (var i = 0; i < state.reducer.tas.length; i++) {
    ta_names.push(state.reducer.tas[i].firstname + ' ' + state.reducer.tas[i].lastname);
  }
  return {
    submitRollShow: state.reducer.submitRollShow,
    submitLeaveSlipShow: state.reducer.submitLeaveSlipShow,
    submitGroupLeaveSlipShow: state.reducer.submitGroupLeaveSlipShow,
    otherReasonsShow: state.reducer.otherReasonsShow,
    leaveSlipDetailsShow: state.reducer.leaveSlipDetailsShow,
    selectedEvents: state.reducer.selectedEvents,
    submitting: state.reducer.submitting,
    formSuccess: state.reducer.formSuccess,
    trainee: state.reducer.trainee,
    tas: ta_names,
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
    },
    postRollSlip: (rollSlip, selectedEvents, slipId) => { //slipId here will be null
      dispatch(postRollSlip(rollSlip, selectedEvents, slipId))
    },
    postGroupLeaveSlip: (gSlip, selectedEvents) => {
      dispatch(postGroupLeaveSlip(gSlip, selectedEvents))
    }
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions