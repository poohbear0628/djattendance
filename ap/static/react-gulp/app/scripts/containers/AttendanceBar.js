import { connect } from 'react-redux'
import { toggleUnexcusedAbsences, toggleUnexcusedTardies, toggleExcused } from '../actions'
import AttendanceDetails from '../components/AttendanceDetails'

const mapStateToProps = (state) => {
  var weekStart = dateFns.format(dateFns.startOfWeek(state.date), 'M/D/YY'),
      weekEnd = dateFns.format(dateFns.endOfWeek(state.date), 'M/D/YY');

  //get just this week's events
  var wesr = _.filter(state.eventsSlipsRolls, function(esr) {
    return (new Date(weekStart) < new Date(esr.event['start']) && new Date(weekEnd) > new Date(esr.event['end']));
  }, this);
  
  var unexcusedAbsences = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip === null || wesr[i].slip["status"] == "D")
           && (wesr[i].roll && wesr[i].roll["status"] == "A")) {
      unexcusedAbsences.push(wesr[i]);
    }
  }

  var unexcusedTardies = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip === null || wesr[i].slip["status"] == "D")
           && (wesr[i].roll && (wesr[i].roll["status"] == "T" || wesr[i].roll["status"] == "U" || wesr[i].roll["status"] == "L"))) {
      unexcusedTardies.push(wesr[i]);
    }
  }

  var excused = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip !== null && wesr[i].slip["status"] == "A")) {
      excused.push(wesr[i]);
    }
  }

  return {
    unexcusedAbsences: unexcusedAbsences,
    unexcusedTardies: unexcusedTardies,
    excused: excused,
    unexcusedAbsencesShow: state.unexcusedAbsencesShow,
    unexcusedTardiesShow: state.unexcusedTardiesShow,
    excusedShow: state.excusedShow
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onAbsencesToggle: () => {
      dispatch(toggleUnexcusedAbsences())
    },
    onTardiesToggle: () => {
      dispatch(toggleUnexcusedTardies())
    },
    onExcusedToggle: () => {
      dispatch(toggleExcused())
    }
  }
}

const AttendanceBar = connect(
  mapStateToProps,
  mapDispatchToProps
)(AttendanceDetails)

export default AttendanceBar