import { NEXT_WEEK, PREV_WEEK, NEXT_PERIOD, PREV_PERIOD, 
         TOGGLE_UNEXCUSED_ABSENCES, TOGGLE_UNEXCUSED_TARDIES, TOGGLE_EXCUSED, 
         TOGGLE_SUBMIT_ROLL, TOGGLE_SUBMIT_LEAVE_SLIP, TOGGLE_SUBMIT_GROUP_LEAVE_SLIP, 
         TOGGLE_LEAVE_SLIPS, TOGGLE_OTHER_REASONS,
         TOGGLE_EVENT, TOGGLE_DAYS_EVENTS, REMOVE_SELECTED_EVENT, REMOVE_ALL_SELECTED_EVENTS } from '../actions';
import { sortEvents } from '../constants'
import initialState from '../initialState';

function reducer(state = initialState, action) {
  switch (action.type) {
    case PREV_WEEK:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, -7)
      });
    case NEXT_WEEK:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, 7)
      });
    case PREV_PERIOD:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, -14)
      });
    case NEXT_PERIOD:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, 14)
      });
    case TOGGLE_UNEXCUSED_ABSENCES:
      return Object.assign({}, state, {
        unexcusedAbsencesShow: !state.unexcusedAbsencesShow
      });
    case TOGGLE_UNEXCUSED_TARDIES:
      return Object.assign({}, state, {
        unexcusedTardiesShow: !state.unexcusedTardiesShow
      });
    case TOGGLE_EXCUSED:
      return Object.assign({}, state, {
        excusedShow: !state.excusedShow
      });
    case TOGGLE_SUBMIT_ROLL:
      return Object.assign({}, state, {
        submitRollShow: !state.submitRollShow,
        submitGroupLeaveSlipShow: false,
      });
    case TOGGLE_SUBMIT_LEAVE_SLIP:
      return Object.assign({}, state, {
        submitLeaveSlipShow: !state.submitLeaveSlipShow,
        submitGroupLeaveSlipShow: false,
      });
    case TOGGLE_SUBMIT_GROUP_LEAVE_SLIP:
      return Object.assign({}, state, {
        submitRollShow: false,
        submitLeaveSlipShow: false,
        submitGroupLeaveSlipShow: !state.submitGroupLeaveSlipShow
      });
    case TOGGLE_LEAVE_SLIPS:
      return Object.assign({}, state, {
        leaveSlipsShow: !state.leaveSlipsShow
      }); 
    case TOGGLE_OTHER_REASONS:
      return Object.assign({}, state, {
        otherReasonsShow: !state.otherReasonsShow
      });
    case TOGGLE_EVENT:
      for (var i = 0; i < state.selectedEvents.length; i++) {
        if (action.event == state.selectedEvents[i]) {
          state.selectedEvents.splice(i, 1);
          return Object.assign({}, state, {
            selectedEvents: state.selectedEvents.slice()
          });
        }
      }
      var nSE = state.selectedEvents.slice();
      nSE.push(action.event);
      nSE.sort(sortEvents)

      return Object.assign({}, state, {
        selectedEvents: nSE
      });
    case TOGGLE_DAYS_EVENTS:
      var evs = action.events.slice();
      for (var i = 0; i < state.selectedEvents.length; i++) {
        for (var j = 0; j < action.events.length; j++) {
          if (action.events[j] == state.selectedEvents[i]) {
            action.events.splice(j, 1);
          }
        }
      }

      if (action.events.length != 0) {
        return Object.assign({}, state, {
          selectedEvents: state.selectedEvents.concat(action.events).slice()
        });
      }

      for (var i = 0; i < state.selectedEvents.length; i++) {
        for (var j = 0; j < evs.length; j++) {
          if (evs[j] == state.selectedEvents[i]) {
            state.selectedEvents.splice(i, 1);
          }
        }
      }

      return Object.assign({}, state, {
        selectedEvents: state.selectedEvents.slice()
      });
    case REMOVE_SELECTED_EVENT:
      for (var i = 0; i < state.selectedEvents.length; i++) {
        if (action.event == state.selectedEvents[i]) {
          state.selectedEvents.splice(i, 1);
        }
      }
      return Object.assign({}, state, {
        selectedEvents: state.selectedEvents.slice()
      });
    case REMOVE_ALL_SELECTED_EVENTS:
      return Object.assign({}, state, {
        selectedEvents: []
      });
    default:
      return state;
  }
}

export default reducer