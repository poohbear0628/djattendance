//set manipulations used to do array computations easily from https://www.npmjs.com/package/set-manipulator
import { union, intersection, difference, complement, equals } from 'set-manipulator';

import { NEXT_WEEK, PREV_WEEK, NEXT_PERIOD, PREV_PERIOD, SUBMIT_ROLL, TOGGLE_ROLL, TOGGLE_LEAVESLIP, TOGGLE_GROUPSLIP, VIEW_LEAVESLIP, VIEW_GROUPSLIP, HIDE_ALL_FORMS, TOGGLE_EVENT, TOGGLE_DAYS_EVENTS, DESELECT_EVENT, DESELECT_ALL_EVENTS, DESTROY_LEAVESLIP, SUBMIT_LEAVESLIP, SUBMIT_GROUPSLIP, DESTROY_GROUPSLIP
          } from '../actions';
import { LEAVE_SLIP_OTHER_TYPES, sortEvents } from '../constants'
import initialState from '../initialState';
import {reducer as formReducer} from 'redux-form';
import { combineReducers } from 'redux'

function date(state = initialState.date, action) {
  switch (action.type) {
    //WeekNav
    case PREV_WEEK:
      return dateFns.addDays(state, -7);
    case NEXT_WEEK:
      return dateFns.addDays(state, 7);
    case PREV_PERIOD:
      return dateFns.addDays(state, -14);
    case NEXT_PERIOD:
      return dateFns.addDays(state, 14);
    default:
      return state;
  }
}

function rolls(state = initialState.rolls, action) {
  switch (action.type) {
    //Async related (action.roll is returned from ajax call)
    case SUBMIT_ROLL:
      //remove all old rolls with complement (arr1-arr2)
      //merge with new rolls
      return [
        ...complement(state, action.rolls),
        ...action.roll
      ];
    default:
      return state;
  }
}

//manages toggle state for various actions
function toggle(state = false, action) {
  switch (action.type) {
    case TOGGLE_ROLL: 
      return Object.assign({}, state, {
        roll: !state.roll
      });
    case TOGGLE_LEAVESLIP:
      return Object.assign({}, state, {
        leaveslip: !state.leaveslip,
        groupslip: false
      });
    case TOGGLE_GROUPSLIP:
      return Object.assign({}, state, {
        groupslip: !state.groupslip,
        leaveslip: false
      });
    case VIEW_LEAVESLIP:
      return Object.assign({}, state, {
        leaveslip: true,
        groupslip: false,
        roll: false
      });
    case VIEW_GROUPSLIP:
      return Object.assign({}, state, {
        leaveslip: false,
        groupslip: true,
        roll: false
      });
    case HIDE_ALL_FORMS:
      return Object.assign({}, state, {
        leaveslip: false,
        groupslip: false,
        roll: false
      });
    //do something only if nothing is showing
    case TOGGLE_EVENT:
    case TOGGLE_DAYS_EVENTS:
      if(!state.roll && !state.leaveslip) {
        return Object.assign({}, state, {
          roll: true
        });  
      } else {
        return state;
      }
    default:
      return state;
  }
}

function selectedEvents(state=[], action) {
  switch (action.type) {
    case TOGGLE_EVENT:
      // if event is in state
      if(intersection(state, [action.event], (ev) => ev.id).length == 1) {
        return complement(state, [action.event], (ev) => ev.id)
      } else {
        return union(state, [action.event], (ev) => ev.id)
      }
    case TOGGLE_DAYS_EVENTS:
      // if all events are in the state, remove them
      if(intersection(state, action.events, (ev) => ev.id).length == action.events.length) {
        return complement(state, action.event, (ev) => ev.id)
      } else {
        return union(state, action.event, (ev) => ev.id)
      }
    case VIEW_LEAVESLIP:
      return action.events;
    case DESELECT_EVENT:
      return complement(state, action.event, (ev) => ev.id)
    case DESELECT_ALL_EVENTS:
    case DESTROY_LEAVESLIP:
    case SUBMIT_ROLL:
    case SUBMIT_LEAVESLIP:
    case SUBMIT_GROUPSLIP:
      return [];
    default:
      return state;
  }
}

function leaveslips(state = initialState.leaveslips, action) {
  switch (action.type) {
    case SUBMIT_LEAVESLIP:
      return [
        ...state,
        action.leaveslip
      ];
    case DESTROY_LEAVESLIP:
      return complement(state, [action.leaveslip], (ls) => ls.id)
    default:
      return state;
  }
}

function groupslips(state = initialState.groupslips, action) {
  switch (action.type) {
    case SUBMIT_GROUPSLIP:
      return [
        ...state,
        action.groupslip
      ];
    case DESTROY_GROUPSLIP:
      return complement(state, [action.groupslip], (ls) => ls.id)
    default:
      return state;
  }
}

const reducers = {
  //static variables that will never mutate 
  events: (state = {}) => state,
  trainee: (state = {}) => state,
  trainees: (state = {}) => state,
  isSecondYear: (state = {}) => state,
  tas: (state = {}) => state,
  term: (state = {}) => state,
  
  //these will mutate...
  submitting: (state = {}) => state,
  formSuccess: (state = {}) => state,
  
  // variables that will mutate
  date,
  toggle,
  selectedEvents,
  rolls,
  leaveslips,
  groupslips,
  form: formReducer
}

const combined = combineReducers(reducers);

export default combined;