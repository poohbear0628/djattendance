import { connect } from 'react-redux'
import { nextWeek, prevWeek, prevPeriod, nextPeriod } from '../actions'
import { getDateDetails } from '../selectors/selectors'
import WeekBar from '../components/WeekBar'

const mapStateToProps = (state) => {
<<<<<<< HEAD
  let details = getDateDetails(state)
  details.traineeView = state.form.traineeView
  return details
=======
  return getDateDetails(state)
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
}

const mapDispatchToProps = (dispatch) => {
  return {
    onPrevWeek: () => {
      dispatch(prevWeek())
    },
    onNextWeek: () => {
      dispatch(nextWeek())
    },
    onPrevPeriod: () => {
      dispatch(prevPeriod())
    },
    onNextPeriod: () => {
      dispatch(nextPeriod())
    }
  }
}

const WeekNav = connect(
  mapStateToProps,
  mapDispatchToProps
)(WeekBar)

<<<<<<< HEAD
export default WeekNav
=======
export default WeekNav
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
