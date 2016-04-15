import {reset} from 'redux-form';
import initialState from './initialState'

//action types
//action creators
//WeekNav
export const NEXT_WEEK = 'NEXT_WEEK'
export const nextWeek = () => {
  return {type: NEXT_WEEK};
}

export const PREV_WEEK = 'PREV_WEEK'
export const prevWeek = () => {
  return {type: PREV_WEEK};
}

export const NEXT_PERIOD = 'NEXT_PERIOD'
export const nextPeriod = () => {
  return {type: NEXT_PERIOD};
}

export const PREV_PERIOD = 'PREV_PERIOD'
export const prevPeriod = () => {
  return {type: PREV_PERIOD};
}

//AttendanceBar
export const TOGGLE_UNEXCUSED_ABSENCES = 'TOGGLE_UNEXCUSED_ABSENCES'
export const toggleUnexcusedAbsences = () => {
  return {type: TOGGLE_UNEXCUSED_ABSENCES};
}

export const TOGGLE_UNEXCUSED_TARDIES = 'TOGGLE_UNEXCUSED_TARDIES'
export const toggleUnexcusedTardies = () => {
  return {type: TOGGLE_UNEXCUSED_TARDIES};
}

export const TOGGLE_EXCUSED = 'TOGGLE_EXCUSED'
export const toggleExcused = () => {
  return {type: TOGGLE_EXCUSED};
}

export const TOGGLE_LEAVE_SLIPS = 'TOGGLE_LEAVE_SLIPS'
export const toggleLeaveSlips = () => {
  return {type: TOGGLE_LEAVE_SLIPS};
}

//AttendanceActions
export const TOGGLE_SUBMIT_ROLL = 'TOGGLE_SUBMIT_ROLL'
export const toggleSubmitRoll = () => {
  return {type: TOGGLE_SUBMIT_ROLL};
}

export const TOGGLE_SUBMIT_LEAVE_SLIP = 'TOGGLE_SUBMIT_LEAVE_SLIP'
export const toggleSubmitLeaveSlip = () => {
  return {type: TOGGLE_SUBMIT_LEAVE_SLIP};
}

export const TOGGLE_SUBMIT_GROUP_LEAVE_SLIP = 'TOGGLE_SUBMIT_GROUP_LEAVE_SLIP'
export const toggleSubmitGroupLeaveSlip = () => {
  return {type: TOGGLE_SUBMIT_GROUP_LEAVE_SLIP};
}

export const TOGGLE_OTHER_REASONS = 'TOGGLE_OTHER_REASONS'
export const toggleOtherReasons = () => {
  return {type: TOGGLE_OTHER_REASONS};
}

export const REMOVE_SELECTED_EVENT = 'REMOVE_SELECTED_EVENT'
export const removeSelectedEvent = (ev) => {
  return {type: REMOVE_SELECTED_EVENT, event: ev};
}

export const REMOVE_ALL_SELECTED_EVENTS = 'REMOVE_ALL_SELECTED_EVENTS'
export const removeAllSelectedEvents = () => {
  return {type: REMOVE_ALL_SELECTED_EVENTS};
}

export const DISMISS_ALERT = 'DISMISS_ALERT'
export const dismissAlert = () => {
  return {type: DISMISS_ALERT};
}

//GridContainer
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const toggleEvent = (ev) => {
  return {type: TOGGLE_EVENT, event: ev};
}

export const TOGGLE_DAYS_EVENTS = 'TOGGLE_DAYS_EVENTS' 
export const toggleDaysEvents = (evs) => {
  return {type: TOGGLE_DAYS_EVENTS, events: evs};
}

//async related
export const SUBMIT_ROLL = 'SUBMIT_ROLL'
export const submitRoll = (roll) => {
  return {
    type: SUBMIT_ROLL,
    roll: roll
  }
}

//this is a thunk
export const postRoll = (rollStatus, selectedEvents) => {

  var rolls = [];
  var roll = {
      "id": null, 
      "event": null, 
      "trainee": initialState.reducer.trainee.id, 
      "status": rollStatus.rollStatus,
      "finalized": false, 
      "notes": "", 
      "submitted_by": initialState.reducer.trainee.id, 
      "last_modified": Date.now()
    }
  if (selectedEvents.length == 0) {
    //need to create an error action
    return function (dispatch) {
      dispatch(receiveResponse('error no events selected'));
    }
  }
  else {
    for (var i = 0; i < selectedEvents.length; i++) {
      rolls.push(Object.assign({}, roll, {
        event: selectedEvents[i].id
      }));
    }
  }
  return function (dispatch) {
    console.log('rolls: ', rolls);

    dispatch(submitRoll(rolls));

    var data = null;
    if (rolls.length == 1) {
      data = rolls[0];
    } else {
      data = JSON.stringify(rolls);
    }

    return $.ajax({
      url: 'http://localhost:8000/api/rolls/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(rolls),
      success: function (data, status, jqXHR) {
        console.log(data, status, jqXHR);
        dispatch(receiveResponse(status));
        dispatch(reset('rollForm'));
        dispatch(removeAllSelectedEvents());
      }
    });

      // In a real world app, you also want to
      // catch any error in the network call.
  }
}

export const SUBMIT_LEAVE_SLIP = 'SUBMIT_LEAVE_SLIP'
function submitLeaveSlip(slip) {
  return {
    type: SUBMIT_LEAVE_SLIP,
    slip: slip
  }
}

export function postLeaveSlip(slipValues) {
  if (slipValues.selectedEvents.length == 0) {
    //need to create an error action
    return function (dispatch) {
      dispatch(receiveResponse('error no events selected'));
    }
  }
  var tas = initialState.reducer.tas;
  var ta_id = null;
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    if (slipValues.TAInformed == tas[i].firstname + ' ' + tas[i].lastname) {
      ta_id = tas[i].id
    }
  }

  var event_ids = [];
  for (var i = 0; i < slipValues.selectedEvents.length; i++) {
    event_ids.push(slipValues.selectedEvents[i].id);
  }
  var slip = {
        "id": null, 
        "type": slipValues.slipReason,
        "status": "P", 
        "TA": ta_id, 
        "trainee": initialState.reducer.trainee.id, 
        "submitted": Date.now(), 
        "last_modified": Date.now(), 
        "finalized": null, 
        "description": "", 
        "comments": slipValues.comments, 
        "texted": !slipValues.informStatus, 
        "informed": slipValues.informStatus, 
        "events": event_ids
    };

  console.log('slip: ', slip);
  return function (dispatch) {
    dispatch(submitLeaveSlip(slip));

    return $.ajax({
      url: 'http://localhost:8000/api/individualleaveslips/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(slip),
      success: function (data, status, jqXHR) {
        console.log(data, status, jqXHR);
        dispatch(receiveResponse(status));
        dispatch(reset('slipForm'));
        dispatch(removeAllSelectedEvents());
      }
    });
  }
}

export const RECEIVE_RESPONSE = 'RECEIVE_RESPONSE'
function receiveResponse(response) {
  return {
    type: RECEIVE_RESPONSE,
    response: response,
    receivedAt: Date.now()
  }
}

