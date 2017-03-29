import { connect } from 'react-redux'
import { postLeaveSlip, changeLeaveSlipForm } from '../actions'
import LeaveSlipForm from '../components/LeaveSlipForm'

const mapStateToProps = (state) => {
  return {
    form: {
      selectedEvents: state.selectedEvents,
      slipType: state.form.leaveSlip.slipType,
      ta_informed: state.form.leaveSlip.ta_informed,
      ta: state.form.leaveSlip.ta,
      comment: state.form.leaveSlip.comment,
      trainee: state.trainee,
    },
    tas: state.tas,
  }
}
const mapDispatchToProps = (dispatch) => {
  return {    
    postLeaveSlip: (values) => { dispatch(postLeaveSlip(values)) },
    changeLeaveSlipForm: (values) => { dispatch(changeLeaveSlipForm(values)) }
  }
}

const LeaveSlipPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(LeaveSlipForm)

export default LeaveSlipPane