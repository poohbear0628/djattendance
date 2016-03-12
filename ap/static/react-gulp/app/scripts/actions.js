//action types
export const NEXT_WEEK = 'NEXT_WEEK'
export const PREV_WEEK = 'PREV_WEEK'
export const NEXT_PERIOD = 'NEXT_PERIOD'
export const PREV_PERIOD = 'PREV_PERIOD'
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const SET_ROLL_STATUS = 'SET_ROLL_STATUS'
export const TOGGLE_UNEXCUSED_ABSENCES = 'TOGGLE_UNEXCUSED_ABSENCES'
export const TOGGLE_UNEXCUSED_TARDIES = 'TOGGLE_UNEXCUSED_TARDIES'
export const TOGGLE_EXCUSED = 'TOGGLE_EXCUSED'

//action creators
//http://rackt.org/redux/docs/basics/Actions.html
//https://github.com/acdlite/flux-standard-action
export const nextWeek = () => {
  return {type: NEXT_WEEK};
}

export const prevWeek = () => {
  return {type: PREV_WEEK};
}

export const nextPeriod = () => {
  return {type: NEXT_PERIOD};
}

export const prevPeriod = () => {
  return {type: PREV_PERIOD};
}

export const toggleEvent = (ev) => {
  return {type: TOGGLE_EVENT, ev};
}

export const setRollStatus = (status) => {
  return {type: SET_ROLL_STATUS, status};
}

export const toggleUnexcusedAbsences = () => {
  return {type: TOGGLE_UNEXCUSED_ABSENCES};
}

export const toggleUnexcusedTardies = () => {
  return {type: TOGGLE_UNEXCUSED_TARDIES};
}

export const toggleExcused = () => {
  return {type: TOGGLE_EXCUSED};
}