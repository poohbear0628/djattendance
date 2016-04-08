//action types
export const NEXT_WEEK = 'NEXT_WEEK'
export const PREV_WEEK = 'PREV_WEEK'
export const NEXT_PERIOD = 'NEXT_PERIOD'
export const PREV_PERIOD = 'PREV_PERIOD'
export const TOGGLE_UNEXCUSED_ABSENCES = 'TOGGLE_UNEXCUSED_ABSENCES'
export const TOGGLE_UNEXCUSED_TARDIES = 'TOGGLE_UNEXCUSED_TARDIES'
export const TOGGLE_EXCUSED = 'TOGGLE_EXCUSED'
export const TOGGLE_SUBMIT_ROLL = 'TOGGLE_SUBMIT_ROLL'
export const TOGGLE_SUBMIT_LEAVE_SLIP = 'TOGGLE_SUBMIT_LEAVE_SLIP'
export const TOGGLE_SUBMIT_GROUP_LEAVE_SLIP = 'TOGGLE_SUBMIT_GROUP_LEAVE_SLIP'
export const TOGGLE_LEAVE_SLIPS = 'TOGGLE_LEAVE_SLIPS'
export const TOGGLE_OTHER_REASONS = 'TOGGLE_OTHER_REASONS'
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const TOGGLE_DAYS_EVENTS = 'TOGGLE_DAYS_EVENTS' 
export const REMOVE_SELECTED_EVENT = 'REMOVE_SELECTED_EVENT'
export const REMOVE_ALL_SELECTED_EVENTS = 'REMOVE_ALL_SELECTED_EVENTS'

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

export const toggleUnexcusedAbsences = () => {
  return {type: TOGGLE_UNEXCUSED_ABSENCES};
}

export const toggleUnexcusedTardies = () => {
  return {type: TOGGLE_UNEXCUSED_TARDIES};
}

export const toggleExcused = () => {
  return {type: TOGGLE_EXCUSED};
}

export const toggleSubmitRoll = () => {
  return {type: TOGGLE_SUBMIT_ROLL};
}

export const toggleSubmitLeaveSlip = () => {
  return {type: TOGGLE_SUBMIT_LEAVE_SLIP};
}

export const toggleSubmitGroupLeaveSlip = () => {
  return {type: TOGGLE_SUBMIT_GROUP_LEAVE_SLIP};
}

export const toggleLeaveSlips = () => {
  return {type: TOGGLE_LEAVE_SLIPS};
}

export const toggleOtherReasons = () => {
  return {type: TOGGLE_OTHER_REASONS};
}

export const toggleEvent = (ev) => {
  return {type: TOGGLE_EVENT, event: ev};
}

export const toggleDaysEvents = (evs) => {
  return {type: TOGGLE_DAYS_EVENTS, events: evs};
}

export const removeSelectedEvent = (ev) => {
  return {type: REMOVE_SELECTED_EVENT, event: ev};
}

export const removeAllSelectedEvents = () => {
  return {type: REMOVE_ALL_SELECTED_EVENTS};
}