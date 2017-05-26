import { connect } from 'react-redux'
import { postLeaveSlip, changeLeaveSlipForm, resetLeaveslipForm } from '../actions'
import { lastLeaveslips } from '../selectors/selectors'
import LeaveSlipForm from '../components/LeaveSlipForm'

const mapStateToProps = (state) => {
  return {
    lastSlips: lastLeaveslips(state),
    form: {
      ...state.form.leaveSlip,
      selectedEvents: state.selectedEvents,
      trainee: state.trainee,
    },
    tas: state.tas,
  }
}
const mapDispatchToProps = (dispatch) => {
  return {
    postLeaveSlip: (values) => { console.log(values); dispatch(postLeaveSlip(values)) },
    changeLeaveSlipForm: (values) => { console.log(values); dispatch(changeLeaveSlipForm(values)) },
    resetForm: () => { dispatch(resetLeaveslipForm()) },
  }
}

const LeaveSlipPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(LeaveSlipForm)

export default LeaveSlipPane
