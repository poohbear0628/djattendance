import { NEXT_WEEK, PREV_WEEK, NEXT_PERIOD, PREV_PERIOD, 
         TOGGLE_UNEXCUSED_ABSENCES, TOGGLE_UNEXCUSED_TARDIES, TOGGLE_EXCUSED, TOGGLE_LEAVE_SLIPS,
         TOGGLE_SUBMIT_ROLL, TOGGLE_SUBMIT_LEAVE_SLIP, TOGGLE_SUBMIT_GROUP_LEAVE_SLIP, TOGGLE_OTHER_REASONS,
         REMOVE_SELECTED_EVENT, REMOVE_ALL_SELECTED_EVENTS, DISMISS_ALERT, TOGGLE_EVENT, TOGGLE_DAYS_EVENTS, 
         SUBMIT_ROLL, SUBMIT_LEAVE_SLIP, RECEIVE_RESPONSE } from '../actions';
import { sortEvents } from '../constants'
import initialState from '../initialState';

function reducer(state = initialState, action) {
  switch (action.type) {
    //WeekNav
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
    //AttendanceBar
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
    case TOGGLE_LEAVE_SLIPS:
      return Object.assign({}, state, {
        leaveSlipsShow: !state.leaveSlipsShow
      }); 
    //AttendanceActions
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
    case TOGGLE_OTHER_REASONS:
      return Object.assign({}, state, {
        otherReasonsShow: !state.otherReasonsShow
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
    case DISMISS_ALERT:
      return Object.assign({}, state, {
        formSuccess: null
      })
    //GridContainer
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
    //Async related
    case SUBMIT_ROLL:
      console.log('action.roll: ', action.roll);
      if (action.roll.length == 1) {
        for (var i = 0; i < state.eventsSlipsRolls.length; i++) {
          if (state.eventsSlipsRolls[i].event.id == action.roll[0].event) {
            state.eventsSlipsRolls[i].roll = action.roll[0];
          }
        }

        var nEsr = state.eventsSlipsRolls.slice();

        return Object.assign({}, state, {
          submitting: true,
          eventsSlipsRolls: nEsr,
          rolls: [
            ...state.rolls,
            action.roll[0]
          ]
        });
      } else {
        //TO-DO handle array of rolls
        console.log('TODO');
        for (var i = 0; i < state.eventsSlipsRolls.length; i++) {
          for (var j = 0; j < action.roll.length; j++) {
            if (state.eventsSlipsRolls[i].event.id == action.roll[j].event) {
              state.eventsSlipsRolls[i].roll = action.roll[j];
            }
          }
        }
        var nEsr = state.eventsSlipsRolls.slice();
        var nRolls = state.rolls.concat(action.roll);
        return Object.assign({}, state, {
          submitting: true,
          eventsSlipsRolls: nEsr,
          rolls: nRolls
        });
      }
    case SUBMIT_LEAVE_SLIP:
      console.log('action.slip: ', action.slip);
      for (var i = 0; i < state.eventsSlipsRolls.length; i++) {
        for (var j = 0; j < action.slip.events.length; j++) {
          if (state.eventsSlipsRolls[i].event.id == action.slip.events[j]) {
            state.eventsSlipsRolls[i].slip = action.slip;
            break;
          }
        }
      }

      var nEsr = state.eventsSlipsRolls.slice();
      console.log('HEREASDKFJA');
      return Object.assign({}, state, {
        submitting: true,
        eventsSlipsRolls: nEsr,
        slips: [
          ...state.slips,
          action.slip
        ]
      });
    case RECEIVE_RESPONSE:
      return Object.assign({}, state, {
        submitting: false
      });
    default:
      return state;
  }
}

export default reducer