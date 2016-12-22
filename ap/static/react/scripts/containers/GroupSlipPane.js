import { connect } from 'react-redux'
import { postGroupSlip, changeGroupSlipForm } from '../actions'
import { traineeMultiSelect }from "../selectors/selectors"
import GroupSlipForm from '../components/GroupSlipForm'

const mapStateToProps = (state) => {
  console.log(state)
  return {
    form: {
      slipType: state.form.groupSlip.slipType,
      events: state.events,
      selectedEvents: state.selectedEvents,
      ta_informed: state.form.groupSlip.ta_informed,
      ta: state.form.groupSlip.ta,
      comment: state.form.groupSlip.comment,
      trainee: state.trainee,
      trainees: state.form.groupSlip.trainees,
      start_time: state.form.groupSlip.start_time,
      end_time: state.form.groupSlip.end_time,
    },
    tas: state.tas,
    trainees: traineeMultiSelect(state),
  }
}
const mapDispatchToProps = (dispatch) => {
  return {    
    postGroupSlip: (values) => { dispatch(postGroupSlip(values)) },
    changeGroupSlipForm: (values) => { dispatch(changeGroupSlipForm(values)) }
  }
}

const GroupSlipPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(GroupSlipForm)

export default GroupSlipPane