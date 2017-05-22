import { connect } from 'react-redux'
import { changeDate, selectPeriod } from '../actions'
import { getDateDetails } from '../selectors/selectors'
import WeekBar from '../components/WeekBar'

const mapStateToProps = (state) => {
  let details = getDateDetails(state)
  details.traineeView = state.form.traineeView
  return details
}

const mapDispatchToProps = (dispatch) => {
  return {
    onPrevWeek: () => {
      dispatch(changeDate(-7))
    },
    onNextWeek: () => {
      dispatch(changeDate(7))
    },
    onPrevPeriod: () => {
      dispatch(changeDate(-14))
    },
    onNextPeriod: () => {
      dispatch(changeDate(14))
    },
    selectPeriod: (period) => {
      dispatch(selectPeriod(period.value))
    }
  }
}

const WeekNav = connect(
  mapStateToProps,
  mapDispatchToProps,
)(WeekBar)

export default WeekNav
