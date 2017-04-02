import { connect } from 'react-redux'
import { selectTab, showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  return {
    show: state.show,
    isSecondYear: state.isSecondYear,
    trainee: state.trainee
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
