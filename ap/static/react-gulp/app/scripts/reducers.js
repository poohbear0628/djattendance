import { combineReducers } from 'redux'
import { NEXT_WEEK, PREV_WEEK, TOGGLE_EVENT, SET_ROLL_STATUS, RollConstants, SlipConstants } from './actions'
import initialState from './initialState'
var date = moment()

function handleWeek(state = date, action) {
  switch (action.type) {
    case PREV_WEEK:
      console.log('PREV_WEEK')
      return Object.assign({}, state, {
        date: action.date.add(-7, 'd')
      })
    case NEXT_WEEK:
      return Object.assign({}, state, {
        date: action.date.add(7, 'd')
      })
    default:
      return state
  }
}

export default handleWeek