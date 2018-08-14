import { connect } from 'react-redux'
import { postGroupSlip, changeGroupSlipForm, resetGroupslipForm, duplicateSlip, deleteGroupSlip } from '../actions'
import { lastLeaveslips } from '../selectors/selectors'
import GroupSlipForm from '../components/GroupSlipForm'

const mapStateToProps = (state) => {
  var groupslip = null;
  if (state.form.groupSlip.id) {
    for (var i = 0; i < state.groupslips.length; i++) {
      if (state.groupslips[i].id == state.form.groupSlip.id) {
        groupslip = state.groupslips[i];
      }
    }
  }

  if (groupslip) {
    for (var i = 0; i< state.trainees.length; i++) {
      if (state.trainees[i].id == groupslip.trainee) {
        groupslip['submitter_name'] = state.trainees[i].name;
      }
    }
  }

  return {
    form: {
      ...state.form.groupSlip,
      events: state.events,
      selectedEvents: state.selectedEvents,
      trainee: state.trainee,
      traineeView: state.form.traineeView
    },
    tas: state.tas,
    trainees: state.trainees,
    trainee: state.trainee,
    isTAView: state.isTAView,
    groupslip: groupslip
  }
}
const mapDispatchToProps = (dispatch) => {
  return {
    postGroupSlip: (values) => { dispatch(postGroupSlip(values)) },
    changeGroupSlipForm: (values) => { dispatch(changeGroupSlipForm(values)) },
    resetForm: () => { dispatch(resetGroupslipForm()) },
    duplicateSlip: (values) => { dispatch(duplicateSlip(values)) },
    deleteSlip: (slip) => { dispatch(deleteGroupSlip(slip)) },
  }
}

const GroupSlipPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(GroupSlipForm)

export default GroupSlipPane
