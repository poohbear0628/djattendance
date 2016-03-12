import { connect } from 'react-redux'
import DaysRow from '../components/DaysRow'

const mapStateToProps = (state) => {
  var daysArray = [];
  var week = dateFns.eachDay(dateFns.startOfWeek(state.date), dateFns.endOfWeek(state.date));
  for(var i = 0; i < 7; i++) {
    var day = {
      name: dateFns.format(week[i], 'ddd'),
      num: dateFns.format(week[i], 'D'),
      isToday: dateFns.isSameDay(week[i], state.date)
    }
    daysArray.push(day);
  }
  return {
    days: daysArray
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
  }
}

const DaysContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(DaysRow)

export default DaysContainer