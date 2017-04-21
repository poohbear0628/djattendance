import { connect } from 'react-redux'
<<<<<<< HEAD
import { selectTab, showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {
  return {
    show: state.show,
    trainee: state.trainee
=======
import { removeEventsShowCalendar, showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {  
  return {    
    show: state.show,
    selectedEvents: state.selectedEvents,
    isSecondYear: state.isSecondYear
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
<<<<<<< HEAD
    onSelectTab: (index) => {
      dispatch(selectTab(index))
    },
=======
    onShowCalendar: (index, show) => {
      dispatch(removeEventsShowCalendar(index, show))
    },
    showRoll,
    showSummary,
    showLeaveslip,
    showGroupslip
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

<<<<<<< HEAD
export default AttendanceActions
=======
export default AttendanceActions
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
