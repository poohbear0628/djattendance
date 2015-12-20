import { combineReducers } from 'redux';
import { NEXT_WEEK, PREV_WEEK, TOGGLE_EVENT, SET_ROLL_STATUS, RollConstants, SlipConstants } from './actions';
import initialState from './initialState';

function handleWeek(state = initialState, action) {
  switch (action.type) {
    case PREV_WEEK:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, -7)
      });
    case NEXT_WEEK:
      return Object.assign({}, state, {
        date: dateFns.addDays(state.date, 7)
      });
    default:
      return state;
  }
}

export default handleWeek;