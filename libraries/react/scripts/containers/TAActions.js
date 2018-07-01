import { connect } from 'react-redux'
import TABar from '../components/TABar'

const mapStateToProps = (state) => {
  return {
    show: state.show,
    trainee: state.trainee,
    traineeView: state.form.traineeView
  }
}

const mapDispatchToProps = (dispatch) => {
  return {}
}

const TAActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(TABar)

export default TAActions
