//action types
export const NEXT_WEEK = 'NEXT_WEEK'
export const PREV_WEEK = 'PREV_WEEK'
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const SET_ROLL_STATUS = 'SET_ROLL_STATUS'

//constants
export const RollConstants = {
    P: 'present',
    A: 'absent',
    T: 'tardy',
    U: 'uniform',
    L: 'left-class'
}

export const SlipConstants = {
    'A': 'approved',
    'P': 'pending',
    'F': 'fellowship',
    'D': 'denied',
    'S': 'approved'
}

//action creators
//https://github.com/acdlite/flux-standard-action
export function nextWeek(date) {
    return {type: NEXT_WEEK, date}
}

export function prevWeek(date) {
    console.log('actions prevWeek', date)
    return {type: PREV_WEEK, date}
}

export function toggleEvent(ev) {
    return {type: TOGGLE_EVENT, ev}
}

export function setRollStatus(status) {
    return {type: SET_ROLL_STATUS, status}
}