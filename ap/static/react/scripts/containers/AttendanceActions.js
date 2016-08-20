import { connect } from 'react-redux'
import { showRoll, showSummary, showLeaveslip, showGroupslip } from '../actions'
import { getTAs, getTraineeSelect, getToggle } from '../selectors/selectors'
import ActionBar from '../components/ActionBar'

const mapStateToProps = (state) => {  
  return {    
    show: state.show,
    isSecondYear: state.isSecondYear
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    showRoll,
    showSummary,
    showLeaveslip,
    showGroupslip
  }
}

const AttendanceActions = connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionBar)

export default AttendanceActions