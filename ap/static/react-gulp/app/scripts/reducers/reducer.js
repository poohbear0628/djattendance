import { NEXT_WEEK, PREV_WEEK, NEXT_PERIOD, PREV_PERIOD, TOGGLE_UNEXCUSED_ABSENCES, TOGGLE_UNEXCUSED_TARDIES, TOGGLE_EXCUSED } from '../actions';
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
    default:
      return state;
  }
}

export default reducer