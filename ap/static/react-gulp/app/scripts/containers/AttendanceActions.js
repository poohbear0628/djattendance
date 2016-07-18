import { connect } from 'react-redux'
import { toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupSlip,
          toggleLeaveSlips, toggleOtherReasons, removeSelectedEvent, removeAllSelectedEvents,
          postRollSlip, postGroupSlip } from '../actions'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  var ta_names = [];
  for (var i = 0; i < state.reducer.tas.length; i++) {
    ta_names.push(state.reducer.tas[i].firstname + ' ' + state.reducer.tas[i].lastname);
  }

  //leave slip details showing?
  //because there is just a single state object for each form we cannot have two of the same form open at the same time
  //this happens when you have a leaveslip detail showing and also the create a new leaveslip form open at the time
  var lsdShow = false;
  for (var key in state.reducer.leaveSlipDetailsShow) {
    if (state.reducer.leaveSlipDetailsShow.hasOwnProperty(key) 
          && state.reducer.leaveSlipDetailsShow[key]) {
      lsdShow = true;
      break;
    }
  }
  var gsdShow = false;
  for (var key in state.reducer.groupSlipDetailsShow) {
    if (state.reducer.groupSlipDetailsShow.hasOwnProperty(key) 
          && state.reducer.groupSlipDetailsShow[key]) {
      gsdShow = true;
      break;
    }
  }

  var trainees = state.reducer.trainees;
  var traineeSelectOptions = [];
  for (var i = 0; i < trainees.length; i++) {
    traineeSelectOptions.push({'value': trainees[i].id, 'label': trainees[i].name});
  }

  return {
    submitRollShow: state.reducer.submitRollShow,
    submitLeaveSlipShow: state.reducer.submitLeaveSlipShow,
    submitGroupLeaveSlipShow: state.reducer.submitGroupLeaveSlipShow,
    otherReasonsShow: state.reducer.otherReasonsShow,
    selectedEvents: state.reducer.selectedEvents,
    submitting: state.reducer.submitting,
    formSuccess: state.reducer.formSuccess,
    trainee: state.reducer.trainee,
    traineeSelectOptions: traineeSelectOptions,
    isSecondYear: state.reducer.isSecondYear,
    tas: ta_names,
    lsdShow: lsdShow,
    gsdShow: gsdShow,
    groupSlipDetailFormValues: state.reducer.groupSlipDetailFormValues
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
    toggleSubmitGroupSlip: () => {
      dispatch(toggleSubmitGroupSlip())
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
    postRollSlip: (rollSlip, selectedEvents, slipId) => { //slipId here will be null, used in AttendanceDetails and SlipDetails to update slips
      dispatch(postRollSlip(rollSlip, selectedEvents, slipId))
    },
    postGroupSlip: (gSlip, selectedEvents, slipId) => { //slipId here will be null, used in SlipDetails to update slips
      dispatch(postGroupSlip(gSlip, selectedEvents))
    }
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions