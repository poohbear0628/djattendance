import { connect } from 'react-redux'
import { nextWeek, prevWeek } from '../actions'
import WeekBar from '../components/WeekBar'

const mapStateToProps = (state) => {
  return {
    startdate: dateFns.format(dateFns.startOfWeek(state.date), 'MMM D'),
    enddate: dateFns.format(dateFns.endOfWeek(state.date), 'MMM D')
  }
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

export default WeekNav