//action types
export const NEXT_WEEK = 'NEXT_WEEK'
export const PREV_WEEK = 'PREV_WEEK'
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const SET_ROLL_STATUS = 'SET_ROLL_STATUS'

//action creators
//https://github.com/acdlite/flux-standard-action
export function nextWeek(date) {
    return {type: NEXT_WEEK}
}

export function prevWeek(date) {
    return {type: PREV_WEEK}
}

export function toggleEvent(ev) {
    return {type: TOGGLE_EVENT, ev}
}

export function setRollStatus(status) {
    return {type: SET_ROLL_STATUS, status}
}

