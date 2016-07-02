import { connect } from 'react-redux'
import { toggleUnexcusedAbsences, toggleUnexcusedTardies, toggleExcused, 
          toggleLeaveSlips, toggleLeaveSlipDetail, toggleOtherReasons,
          postRollSlip, deleteLeaveSlip, postGroupSlip,
          removeSelectedEvent, removeAllSelectedEvents } from '../actions'
import { sortEsr, sortSlips } from '../constants'
import DetailsBar from '../components/DetailsBar'

const mapStateToProps = (state) => {
  var weekStart = dateFns.format(dateFns.startOfWeek(state.reducer.date, {weekStartsOn: 1}), 'M/D/YY'),
      weekEnd = dateFns.format(dateFns.addDays(dateFns.endOfWeek(state.reducer.date, {weekStartsOn: 1}), 1), 'M/D/YY');

  //get just this week's events
  var wesr = _.filter(state.reducer.eventsSlipsRolls, function(esr) {
    return (new Date(weekStart) < new Date(esr.event['start']) && new Date(weekEnd) > new Date(esr.event['end']));
  }, this);

  wesr = wesr.sort(sortEsr);
  
  var unexcusedAbsences = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip === null || wesr[i].slip["status"] == "D" || wesr[i].slip["status"] == "P" || wesr[i].slip["status"] == "F")
           && (wesr[i].roll && wesr[i].roll["status"] == "A")) {
      unexcusedAbsences.push(wesr[i]);
    }
  }
  unexcusedAbsences = unexcusedAbsences.sort(sortEsr);

  var unexcusedTardies = [];
  for (var i = 0; i < wesr.length; i++) {
    if ((wesr[i].slip === null || wesr[i].slip["status"] == "D" || wesr[i].slip["status"] == "P" || wesr[i].slip["status"] == "F")
           && (wesr[i].roll && (wesr[i].roll["status"] == "T" || wesr[i].roll["status"] == "U" || wesr[i].roll["status"] == "L"))) {
      unexcusedTardies.push(wesr[i]);
    }
  }
  unexcusedTardies = unexcusedTardies.sort(sortEsr);

  var excused = [];
  for (var i = 0; i < wesr.length; i++) {
    if (wesr[i].slip && wesr[i].slip["status"] == "A") {
      excused.push(wesr[i]);
    }
  }
  excused = excused.sort(sortEsr);

  return {
    unexcusedAbsences: unexcusedAbsences,
    unexcusedTardies: unexcusedTardies,
    excused: excused,
    unexcusedAbsencesShow: state.reducer.unexcusedAbsencesShow,
    unexcusedTardiesShow: state.reducer.unexcusedTardiesShow,
    excusedShow: state.reducer.excusedShow,
    otherReasonsShow: state.reducer.otherReasonsShow,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    postRollSlip: (rollSlip, selectedEvents, slipId) => {
      dispatch(postRollSlip(rollSlip, selectedEvents, slipId))
    },
    deleteSlip: (slipId) => {
      dispatch(deleteLeaveSlip(slipId))
    },
    postGroupSlip: (groupSlip, selectedEvents) => {
      dispatch(postGroupSlip(groupSlip, selectedEvents))
    },
    onAbsencesToggle: () => {
      dispatch(toggleUnexcusedAbsences())
    },
    onTardiesToggle: () => {
      dispatch(toggleUnexcusedTardies())
    },
    onExcusedToggle: () => {
      dispatch(toggleExcused())
    },
    removeAllSelectedEvents: () => {
      dispatch(removeAllSelectedEvents())
    },
    removeSelectedEvent: (ev) => {
      dispatch(removeSelectedEvent(ev))
    }
  }
}

const AttendanceDetails = connect(
  mapStateToProps,
  mapDispatchToProps
)(DetailsBar)

export default AttendanceDetails