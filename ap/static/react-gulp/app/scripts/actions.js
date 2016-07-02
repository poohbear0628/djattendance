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

//AttendanceDetails
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

export const TOGGLE_LEAVE_SLIP_DETAIL = 'TOGGLE_LEAVE_SLIP_DETAIL'
export const toggleLeaveSlipDetail = (id, evs, slipType, TA, comments, informed, trainees) => {
  return {type: TOGGLE_LEAVE_SLIP_DETAIL, key: id, evs: evs, slipType: slipType, TA: TA, comments: comments, informed: informed, trainees: trainees};
}

export const TOGGLE_GROUP_SLIP_DETAIL = 'TOGGLE_GROUP_SLIP_DETAIL'
export const toggleGroupSlipDetail = (id, start, end, slipType, TA, comments, informed, trainees) => {
  return {type: TOGGLE_GROUP_SLIP_DETAIL, key: id, start: start, end: end, slipType: slipType, TA: TA, comments: comments, informed: informed, trainees: trainees};
}

//AttendanceActions
export const HIDE_ALL_FORMS =' HIDE_ALL_FORMS'
export const hideAllForms = () => {
  return {type: HIDE_ALL_FORMS};
}

export const TOGGLE_SUBMIT_ROLL = 'TOGGLE_SUBMIT_ROLL'
export const toggleSubmitRoll = () => {
  return {type: TOGGLE_SUBMIT_ROLL};
}

export const TOGGLE_SUBMIT_LEAVE_SLIP = 'TOGGLE_SUBMIT_LEAVE_SLIP'
export const toggleSubmitLeaveSlip = () => {
  return {type: TOGGLE_SUBMIT_LEAVE_SLIP};
}

export const TOGGLE_SUBMIT_GROUP_SLIP = 'TOGGLE_SUBMIT_GROUP_SLIP'
export const toggleSubmitGroupSlip = () => {
  return {type: TOGGLE_SUBMIT_GROUP_SLIP};
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

//async related, using thunks, google redux-thunk for more info

// RollSlip has fields {rollStatus, slipType, comments, informed, TAInformed}
// slipId is determine between POST (new slip, slipId == null) or PUT (update slip, slipId != null)
export const postRollSlip = (rollSlip, selectedEvents, slipId) => {
  if ((rollSlip.rollStatus !== undefined || rollSlip.rollStatus != "") 
        && (rollSlip.slipType === undefined || rollSlip.slipType == "")) {
    return function (dispatch) { 
      dispatch(postRoll(rollSlip, selectedEvents));
    }
  }
  else if ((rollSlip.rollStatus === undefined || rollSlip.rollStatus == "") 
            && (rollSlip.slipType !== undefined || rollSlip.slipType != "")) {
    return function (dispatch) { 
      dispatch(postLeaveSlip(rollSlip, selectedEvents, slipId));
    }
  }
  else if ((rollSlip.rollStatus !== undefined || rollSlip.rollStatus != "") 
            && (rollSlip.slipType !== undefined || rollSlip.slipType != "")) {
    return function (dispatch) {
      dispatch(postRoll(rollSlip, selectedEvents, slipId, true));
    }
  }
  else {
    dispatch(receiveResponse('Error no data for roll or slips'));
  }
}

export const SUBMIT_ROLL = 'SUBMIT_ROLL'
export const submitRoll = (roll) => {
  return {
    type: SUBMIT_ROLL,
    roll: roll
  }
}

export const postRoll = (rollSlip, selectedEvents, slipId = null, withSlip = false) => {
  var rolls = [];
  var roll = {
      "id": null, 
      "event": null, 
      "trainee": initialState.reducer.trainee.id, 
      "status": rollSlip.rollStatus,
      "finalized": false, 
      "notes": "", 
      "submitted_by": initialState.reducer.trainee.id, 
      "last_modified": Date.now(),
      "date": null
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
        event: selectedEvents[i].id,
        date: dateFns.format(selectedEvents[i].start, 'YYYY-MM-DD')
      }));
    }
  }
  return function (dispatch) {
    var data = null;
    if (rolls.length == 1) {
      data = rolls[0];
    } else {
      data = JSON.stringify(rolls);
    }

    return $.ajax({
      url: '/api/rolls/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(rolls),
      success: function (data, status, jqXHR) {
        dispatch(submitRoll(rolls));
        if (withSlip) {
          dispatch(postLeaveSlip(rollSlip, selectedEvents, slipId));
        } else {
          dispatch(receiveResponse(status));
          dispatch(reset('rollSlipForm'));
          dispatch(removeAllSelectedEvents());
          dispatch(hideAllForms());
        }
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Roll post error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}

export const SUBMIT_LEAVE_SLIP = 'SUBMIT_LEAVE_SLIP'
export const submitLeaveSlip = (slip) => {
  return {
    type: SUBMIT_LEAVE_SLIP,
    slip: slip
  }
}

export const postLeaveSlip = (rollSlip, selectedEvents, slipId) => {
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

  var event_details = [];
  for (var i = 0; i < selectedEvents.length; i++) {
    event_details.push({"id": selectedEvents[i].id, "date": dateFns.format(selectedEvents[i].start, 'YYYY-MM-DD')});
  }
  var texted = false;
  if (rollSlip.informed == "texted") {
    texted = true;
    rollSlip.informed = false;
  }
  var slip = {
        "id": slipId, 
        "type": rollSlip.slipType,
        "status": "P", 
        "TA": ta_id, 
        "trainee": initialState.reducer.trainee.id, 
        "submitted": Date.now(), 
        "last_modified": Date.now(), 
        "finalized": null, 
        "description": "", 
        "comments": rollSlip.comments, 
        "texted": texted, 
        "informed": rollSlip.informed, 
        "events": event_details
    };

  var ajaxType = 'POST';
  var ajaxData = JSON.stringify(slip);
  if (slipId) {
    ajaxType = 'PATCH';
    ajaxData = JSON.stringify([slip]);
  }

  return function (dispatch) {
    return $.ajax({
      url: '/api/individualslips/',
      type: ajaxType,
      contentType: 'application/json',
      data: ajaxData,
      success: function (data, status, jqXHR) {
        dispatch(submitLeaveSlip(data));
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

//using destroy because delete is an official HTTP action and is used for the thunk
export const DESTROY_LEAVE_SLIP = 'DESTROY_LEAVE_SLIP'
export const destroyLeaveSlip = (slipId) => {
  return {
    type: DESTROY_LEAVE_SLIP,
    slipId: slipId
  }
}

export const deleteLeaveSlip = (slipId) => {
  return function (dispatch) {
    dispatch(destroyLeaveSlip(slipId));
    return $.ajax({
      url: '/api/individualslips/' + slipId.toString(),
      type: 'DELETE',
      success: function (data, status, jqXHR) {
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        dispatch(removeAllSelectedEvents());
        dispatch(hideAllForms());
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Slip delete error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}


export const SUBMIT_GROUP_SLIP = 'SUBMIT_GROUP_SLIP'
export const submitGroupSlip = (gSlip) => {
  return {
    type: SUBMIT_GROUP_SLIP,
    gslip: gSlip,
  }
}

export const postGroupSlip = (gSlip, selectedEvents, slipId) => {
  var tas = initialState.reducer.tas;
  var ta_id = null;
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    if (gSlip.TAInformed == tas[i].firstname + ' ' + tas[i].lastname) {
      ta_id = tas[i].id
    }
  }

  gSlip.start = dateFns.setSeconds(gSlip.start, 0);
  gSlip.end = dateFns.setSeconds(gSlip.end, 0);
  if (typeof gSlip.start == "string" && gSlip.start.indexOf('pm') > -1) {
    gSlip.start = dateFns.addHours(gSlip.start, 12);
  }
  if (typeof gSlip.end == "string" && gSlip.end.indexOf('pm') > -1) {
    gSlip.end = dateFns.addHours(gSlip.end, 12);
  }

  var start = dateFns.format(gSlip.start, "YYYY-MM-DDTHH:mm");
  var end = dateFns.format(gSlip.end, "YYYY-MM-DDTHH:mm");

  // var start = selectedEvents[0].start;
  // var end = selectedEvents[0].end;

  // if (selectedEvents.length > 1) {
  //   for (var i = 1; i < selectedEvents.length; i++) {
  //     if (dateFns.isBefore(selectedEvents[i].start, start)) {
  //       start = selectedEvents[i].start;
  //     }
  //     if (dateFns.isAfter(selectedEvents[i].end, end)) {
  //       end = selectedEvents[i].end;
  //     }
  //   }
  // }

  var texted = false;
  if (gSlip.informed == "texted") {
    texted = true;
    gSlip.informed = false;
  }

  var trainee_ids = [];
  for (var i = 0; i < gSlip.trainees.length; i++) {
    if (gSlip.trainees[i].value) {
      trainee_ids.push(gSlip.trainees[i].value);
    } else {
      trainee_ids.push(gSlip.trainees[i]);
    }
  }
  var slip = {
      "id": slipId,
      "type": gSlip.slipType,
      "status": "P",
      "submitted": Date.now(),
      "last_modified": Date.now(),
      "finalized": null,
      "description": "",
      "comments": gSlip.comments,
      "texted": texted,
      "informed": gSlip.informed,
      "start": start,
      "end": end,
      "TA": ta_id,
      "trainee": null,
      "trainees": trainee_ids
    }

  var ajaxType = 'POST';
  if (slipId) {
    ajaxType = 'PUT';
  }

  return function (dispatch, getState) {
    slip.trainee = getState().reducer.trainee.id;
    var ajaxData = JSON.stringify(slip);
    if (slipId) {
      ajaxData = JSON.stringify([slip]);
    }
    return $.ajax({
      url: '/api/groupslips/',
      type: ajaxType,
      contentType: 'application/json',
      data: ajaxData,
      success: function (data, status, jqXHR) {
        dispatch(submitGroupSlip(data));
        dispatch(receiveResponse(status));
        dispatch(reset('groupSlipForm'));
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

export const DESTROY_GROUP_SLIP = 'DESTROY_GROUP_SLIP'
export const destroyGroupSlip = (slipId) => {
  return {
    type: DESTROY_GROUP_SLIP,
    slipId: slipId
  }
}

export const deleteGroupSlip = (slipId) => {
  return function (dispatch) {
    dispatch(destroyGroupSlip(slipId));
    return $.ajax({
      url: '/api/groupslips/' + slipId.toString(),
      type: 'DELETE',
      success: function (data, status, jqXHR) {
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        dispatch(removeAllSelectedEvents());
        dispatch(hideAllForms());
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Slip delete error!');
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

