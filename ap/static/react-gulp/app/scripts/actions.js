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
export const HIDE_ALL_FORMS =' HIDE_ALL_FORMS'
export const hideAllForms = () => {
  return {type: HIDE_ALL_FORMS}
}

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

// RollSlip has fields {rollStatus, slipReason, comments, informStatus, TAInformed}
export const postRollSlip = (rollSlip, selectedEvents) => {
  console.log('rollSlip: ', rollSlip);
  if (rollSlip.rollStatus !== undefined && rollSlip.slipReason === undefined) {
    return function (dispatch) { 
      dispatch(postRoll(rollSlip, selectedEvents));
    }
  }
  else if (rollSlip.rollStatus === undefined && rollSlip.slipReason !== undefined) {
    return function (dispatch) { 
      dispatch(postLeaveSlip(rollSlip, selectedEvents));
    }
  }
  else if (rollSlip.rollStatus !== undefined && rollSlip.slipReason !== undefined) {
    return function (dispatch) {
      dispatch(postRoll(rollSlip, selectedEvents));
      dispatch(postLeaveSlip(rollSlip, selectedEvents));
    }
  }
  else {
    dispatch(receiveResponse('Error no data for roll or slips'));
  }
}

//this is a thunk
export const postRoll = (rollSlip, selectedEvents) => {
  var rolls = [];
  var roll = {
      "id": null, 
      "event": null, 
      "trainee": initialState.reducer.trainee.id, 
      "status": rollSlip.rollStatus,
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
        // console.log(data, status, jqXHR);
        console.log('Roll post success!');
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        dispatch(removeAllSelectedEvents());
        dispatch(hideAllForms());
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Roll post error!');
        console.log(jqXHR, textStatus, errorThrown);
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

export const postLeaveSlip = (rollSlip, selectedEvents) => {
  if (selectedEvents.length == 0) {
    //need to create an error action
    return function (dispatch) {
      dispatch(receiveResponse('error no events selected'));
    }
  }
  var tas = initialState.reducer.tas;
  var ta_id = null;
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    if (rollSlip.TAInformed == tas[i].firstname + ' ' + tas[i].lastname) {
      ta_id = tas[i].id
    }
  }

  var event_ids = [];
  for (var i = 0; i < selectedEvents.length; i++) {
    event_ids.push(selectedEvents[i].id);
  }
  var texted = false;
  if (rollSlip.informStatus == "texted") {
    texted = true;
    rollSlip.informStatus = false;
  }
  var slip = {
        "id": null, 
        "type": rollSlip.slipReason,
        "status": "P", 
        "TA": ta_id, 
        "trainee": initialState.reducer.trainee.id, 
        "submitted": Date.now(), 
        "last_modified": Date.now(), 
        "finalized": null, 
        "description": "", 
        "comments": rollSlip.comments, 
        "texted": texted, 
        "informed": rollSlip.informStatus, 
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
        // console.log(data, status, jqXHR);
        console.log('Slip post success!');
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        dispatch(removeAllSelectedEvents());
        dispatch(hideAllForms());
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Slip post error!');
        console.log(jqXHR, textStatus, errorThrown);
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

