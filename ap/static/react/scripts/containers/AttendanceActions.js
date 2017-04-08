import { connect } from 'react-redux'
import { removeEventsShowCalendar } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {  
  return {    
    show: state.show,
    selectedEvents: state.selectedEvents,
    isSecondYear: state.isSecondYear
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onShowCalendar: (index, show) => {
      dispatch(removeEventsShowCalendar(index, show))
    }
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions