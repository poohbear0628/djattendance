import { connect } from 'react-redux'
import { postRoll, changeTraineeView, updateRollForm, finalizeRoll } from '../actions'
import { getDateDetails } from '../selectors/selectors.js'
import { canFinalizeRolls } from '../constants.js'
import RollForm from '../components/RollForm'

const mapStateToProps = (state) => {
  let dateDetails = getDateDetails(state)
  return {
    form: {
      selectedEvents: state.selectedEvents,
      rollStatus: state.form.rollStatus,
      trainee: state.trainee,
      trainees: state.trainees,
      traineeView: state.form.traineeView,
    },
    canFinalizeWeek: canFinalizeRolls(state.rolls, dateDetails)
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    postRoll: (values) => { dispatch(postRoll(values)) },
    changeTraineeView: (values) => { dispatch(changeTraineeView(values)) },
    updateRollForm: (values) => { dispatch(updateRollForm(values)) },
    finalizeRoll: () => { dispatch(finalizeRoll()) }
  }
}

const RollPane = connect(
  mapStateToProps,
  mapDispatchToProps
)(RollForm)

export default RollPane
