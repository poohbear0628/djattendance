import { connect } from 'react-redux'
import TraineeSelector from '../components/TraineeSelector'
import { changeTraineeView } from '../actions'

const mapStateToProps = (state) => {
  return {
    form: {
      trainee: state.trainee,
      trainees: state.trainees,
      traineeView: state.form.traineeView
    }
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    changeTraineeView: (values) => { dispatch(changeTraineeView(values)) }
  }
}

const TraineeSelectorContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(TraineeSelector)

export default TraineeSelectorContainer