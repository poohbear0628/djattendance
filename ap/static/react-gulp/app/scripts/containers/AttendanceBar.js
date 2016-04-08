import { connect } from 'react-redux'
import { toggleUnexcusedAbsences, toggleUnexcusedTardies, toggleExcused, toggleLeaveSlips } from '../actions'
import { sortEsr } from '../constants'
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
  unexcusedAbsences = unexcusedAbsences.sort(sortEsr);

  var unexcusedTardies = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip === null || wesr[i].slip["status"] == "D")
           && (wesr[i].roll && (wesr[i].roll["status"] == "T" || wesr[i].roll["status"] == "U" || wesr[i].roll["status"] == "L"))) {
      unexcusedTardies.push(wesr[i]);
    }
  }
  unexcusedTardies = unexcusedTardies.sort(sortEsr);

  var excused = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip !== null && wesr[i].slip["status"] == "A")) {
      excused.push(wesr[i]);
    }
  }
  excused = excused.sort(sortEsr);

  var slips = { 
    pending: [],
    denied: [],
    approved: []
  }
  for (var i = 0; i < wesr.length; i++) {
    if (wesr[i].slip !== null) {
      if (wesr[i].slip["status"] == "A") {
        slips.approved.push(wesr[i]);
      }
      else if (wesr[i].slip["status"] == "D") {
        slips.denied.push(wesr[i]);
      }
      else if (wesr[i].slip["status"] == "P") {
        slips.pending.push(wesr[i]);
      }
    }
  }
  slips.pending = slips.pending.sort(sortEsr);
  slips.denied = slips.denied.sort(sortEsr);
  slips.approved = slips.approved.sort(sortEsr);

  return {
    unexcusedAbsences: unexcusedAbsences,
    unexcusedTardies: unexcusedTardies,
    excused: excused,
    slips: slips,
    unexcusedAbsencesShow: state.unexcusedAbsencesShow,
    unexcusedTardiesShow: state.unexcusedTardiesShow,
    excusedShow: state.excusedShow,
    leaveSlipsShow: state.leaveSlipsShow,
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
    },
    toggleLeaveSlips: () => {
      dispatch(toggleLeaveSlips())
    },
  }
}

const AttendanceBar = connect(
  mapStateToProps,
  mapDispatchToProps
)(AttendanceDetails)

export default AttendanceBar