import { connect } from 'react-redux'
import { toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupSlip,
          toggleLeaveSlips, toggleOtherReasons, removeSelectedEvent, removeAllSelectedEvents,
          postRollSlip, postGroupSlip } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  
  return {
    //state
    isSecondYear: state.isSecondYear,
    selectedEvents: state.selectedEvents,
    trainee: state.trainee,

    //not sure if needed
    submitting: state.submitting,
    formSuccess: state.formSuccess,

    //selectors
    traineeSelectOptions: getTraineeSelect(state),
    tas: getTAs(state),
    toggle: getToggle(state),
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