import { connect } from 'react-redux'
<<<<<<< HEAD
import { removeEventsShowCalendar } from '../actions'
=======
import { selectTab, showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
>>>>>>> f12bf0c9ba532459bfb711e92ebf82997fbbb7e0
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  return {
    show: state.show,
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
