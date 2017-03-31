import { connect } from 'react-redux'
import { postRoll, changeTraineeView, updateRollForm } from '../actions'
import RollForm from '../components/RollForm'

const mapStateToProps = (state) => {
  return {
    form: {
      selectedEvents: state.selectedEvents,
      rollStatus: state.form.rollStatus,
      trainee: state.trainee,
      trainees: state.trainees,
      traineeView: state.form.traineeView,
    }
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    postRoll: (values) => { dispatch(postRoll(values)) },
    changeTraineeView: (values) => { dispatch(changeTraineeView(values)) },
    updateRollForm: (values) => { dispatch(updateRollForm(values)) }
  }
}

const RollPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(RollForm)

export default RollPane
