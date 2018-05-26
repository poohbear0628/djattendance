import { connect } from 'react-redux'
import { selectTab, showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  return {
    show: state.show,
    trainee: state.trainee,
    traineeView: state.form.traineeView
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onSelectTab: (index) => {
      dispatch(selectTab(index))
    },
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions
