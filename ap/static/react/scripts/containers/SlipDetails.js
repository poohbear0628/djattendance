import { connect } from 'react-redux'
import { toggleLeaveSlips, toggleLeaveSlipDetail, toggleGroupSlipDetail, toggleOtherReasons,
          postRollSlip, deleteLeaveSlip, deleteGroupSlip, postGroupSlip,
          removeSelectedEvent, removeAllSelectedEvents } from '../actions'
import { sortEsr, sortSlips } from '../constants'
import LeaveSlipList from '../components/LeaveSlipList'

const mapStateToProps = (state) => {
  var weekStart = dateFns.format(dateFns.startOfWeek(state.date, {weekStartsOn: 1}), 'M/D/YY'),
      weekEnd = dateFns.format(dateFns.addDays(dateFns.endOfWeek(state.date, {weekStartsOn: 1}), 1), 'M/D/YY');

  //get just this week's events
  var wesr = _.filter(state.eventsSlipsRolls, function(esr) {
    return (new Date(weekStart) < new Date(esr.event['start']) && new Date(weekEnd) > new Date(esr.event['end']));
  }, this);

  wesr = wesr.sort(sortEsr);

  var slips = { 
    pending: [],
    denied: [],
    approved: []
  }
  var gslips = {
    pending: [],
    denied: [],
    approved: []
  }
  for (var i = 0; i < wesr.length; i++) {
    if (wesr[i].slip !== null) {
      if ((wesr[i].slip["status"] == "A" || wesr[i].slip["status"] == "S") && _.indexOf(slips.approved, wesr[i].slip) == -1) {
        slips.approved.push(wesr[i].slip);
      }
      else if (wesr[i].slip["status"] == "D" && _.indexOf(slips.denied, wesr[i].slip) == -1) {
        slips.denied.push(wesr[i].slip);
      }
      else if ((wesr[i].slip["status"] == "P" || wesr[i].slip["status"] == "F") && _.indexOf(slips.pending, wesr[i].slip) == -1) {
        slips.pending.push(wesr[i].slip);
      }
    }
    if (wesr[i].gslip !== null) {
      if ((wesr[i].gslip["status"] == "A" || wesr[i].gslip["status"] == "S") && _.indexOf(gslips.approved, wesr[i].gslip) == -1) {
        gslips.approved.push(wesr[i].gslip);
      }
      else if (wesr[i].gslip["status"] == "D" && _.indexOf(gslips.denied, wesr[i].gslip) == -1) {
        gslips.denied.push(wesr[i].gslip);
      }
      else if ((wesr[i].gslip["status"] == "P" || wesr[i].gslip["status"] == "F") && _.indexOf(gslips.pending, wesr[i].gslip) == -1) {
        gslips.pending.push(wesr[i].gslip);
      }
    }
  }
  // TODO: fix sorting slips
  // slips.pending = slips.pending.sort(sortSlips);
  // slips.denied = slips.denied.sort(sortSlips);
  // slips.approved = slips.approved.sort(sortSlips);

  var ta_names = [];
  for (var i = 0; i < state.tas.length; i++) {
    ta_names.push(state.tas[i].firstname + ' ' + state.tas[i].lastname);
  }

  var trainees = state.trainees;
  var traineeSelectOptions = [];
  for (var i = 0; i < trainees.length; i++) {
    traineeSelectOptions.push({'value': trainees[i].id, 'label': trainees[i].name});
  }

  return {
    slips: slips,
    gslips: gslips,
    leaveSlipsShow: state.leaveSlipsShow,
    leaveSlipDetailsShow: state.leaveSlipDetailsShow,
    groupSlipDetailsShow: state.groupSlipDetailsShow,
    otherReasonsShow: state.otherReasonsShow,
    selectedEvents: state.selectedEvents,
    tas: ta_names,
    traineeSelectOptions: traineeSelectOptions,
    traineeId: state.trainee.id
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
    postGroupSlip: (groupSlip, selectedEvents, slipId) => {
      dispatch(postGroupSlip(groupSlip, selectedEvents, slipId))
    },
    deleteGroupSlip: (slipId) => {
      dispatch(deleteGroupSlip(slipId))
    },
    toggleLeaveSlips: () => {
      dispatch(toggleLeaveSlips())
    },
    toggleLeaveSlipDetail: (id, evs, slipType, TA, comments, informed) => {
      dispatch(toggleLeaveSlipDetail(id, evs, slipType, TA, comments, informed))
    },
    toggleGroupSlipDetail: (id, start, end, slipType, TA, comments, informed, trainees) => {
      dispatch(toggleGroupSlipDetail(id, start, end, slipType, TA, comments, informed, trainees))
    },
    toggleOtherReasons: () => {
      dispatch(toggleOtherReasons())
    },
    removeAllSelectedEvents: () => {
      dispatch(removeAllSelectedEvents())
    },
    removeSelectedEvent: (ev) => {
      dispatch(removeSelectedEvent(ev))
    }
  }
}

const LeaveSlipDetails = connect(
  mapStateToProps,
  mapDispatchToProps
)(LeaveSlipList)

export default LeaveSlipDetails