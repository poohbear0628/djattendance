import {
  reset
}
from 'redux-form';
//we shouldn't have initiatestate in here...
import initialState from './initialstate'

// for a reading on why you need this boilerplate, see
// http://redux.js.org/docs/recipes/ReducingBoilerplate.html


//WeekNav
export const NEXT_WEEK = 'NEXT_WEEK'
export const nextWeek = () => {
  return {
    type: NEXT_WEEK
  };
}

export const PREV_WEEK = 'PREV_WEEK'
export const prevWeek = () => {
  return {
    type: PREV_WEEK
  };
}

export const NEXT_PERIOD = 'NEXT_PERIOD'
export const nextPeriod = () => {
  return {
    type: NEXT_PERIOD
  };
}

export const PREV_PERIOD = 'PREV_PERIOD'
export const prevPeriod = () => {
  return {
    type: PREV_PERIOD
  };
}

//toggles

export const TOGGLE_ROLL = 'TOGGLE_ROLL'
export const toggleRoll = () => {
  return {
    type: TOGGLE_ROLL
  };
}

export const TOGGLE_LEAVESLIP = 'TOGGLE_LEAVESLIP'
export const toggleLeaveSlip = () => {
  return {
    type: TOGGLE_LEAVESLIP
  };
}

export const TOGGLE_GROUPSLIP = 'TOGGLE_GROUPSLIP'
export const toggleGroupSlip = () => {
  return {
    type: TOGGLE_GROUPSLIP
  };
}

export const HIDE_ALL_FORMS = ' HIDE_ALL_FORMS'
export const hideAllForms = () => {
  return {
    type: HIDE_ALL_FORMS
  };
}

//GridContainer
export const TOGGLE_EVENT = 'TOGGLE_EVENT'
export const toggleEvent = (ev) => {
  return {
    type: TOGGLE_EVENT,
    event: ev
  };
}

export const TOGGLE_DAYS_EVENTS = 'TOGGLE_DAYS_EVENTS'
export const toggleDaysEvents = (evs) => {
  return {
    type: TOGGLE_DAYS_EVENTS,
    events: evs
  };
}


export const DESELECT_EVENT = 'DESELECT_EVENT'
export const deselectEvent = (ev) => {
  return {
    type: DESELECT_EVENT,
    event: ev
  };
}

export const DESELECT_ALL_EVENTS = 'DESELECT_ALL_EVENTS'
export const deselectAllEvents = () => {
  return {
    type: DESELECT_ALL_EVENTS
  };
}


//async related, using thunks, google redux-thunk for more info

// RollSlip has fields {rollStatus, slipType, comments, informed, TAInformed}
// slipId is determine between POST (new slip, slipId == null) or PUT (update slip, slipId != null)
export const postRollSlip = (rollSlip, selectedEvents, slipId) => {
  if ((rollSlip.rollStatus !== undefined || rollSlip.rollStatus != "") && (rollSlip.slipType === undefined || rollSlip.slipType == "")) {
    return function(dispatch) {
      dispatch(postRoll(rollSlip, selectedEvents));
    }
  } else if ((rollSlip.rollStatus === undefined || rollSlip.rollStatus == "") && (rollSlip.slipType !== undefined || rollSlip.slipType != "")) {
    return function(dispatch) {
      dispatch(postLeaveSlip(rollSlip, selectedEvents, slipId));
    }
  } else if ((rollSlip.rollStatus !== undefined || rollSlip.rollStatus != "") && (rollSlip.slipType !== undefined || rollSlip.slipType != "")) {
    return function(dispatch) {
      dispatch(postRoll(rollSlip, selectedEvents, slipId, true));
    }
  } else {
    dispatch(receiveResponse('Error no data for roll or slips'));
  }
}

export const SUBMIT_ROLL = 'SUBMIT_ROLL'
export const submitRoll = (rolls) => {
  return {
    type: SUBMIT_ROLL,
    rolls: rolls
  }
}

export const postRoll = (values) => {
  var rolls = [];
  var roll = {
    "event": null,
    "trainee": values.traineeView ? values.traineeView.id : values.trainee.id,
    "status": values.rollStatus.id,
    "finalized": false,
    "notes": "",
    "submitted_by": values.trainee.id,
    "last_modified": Date.now(),
    "date": null
  }
  let selectedEvents = values.selectedEvents;
  if (selectedEvents.length == 0) {
    //need to create an error action
    return function(dispatch) {
      dispatch(receiveResponse('error no events selected'));
    }
  } else {
    for (var i = 0; i < selectedEvents.length; i++) {
      rolls.push(Object.assign({}, roll, {
        event: selectedEvents[i].id,
        date: dateFns.format(selectedEvents[i].start, 'YYYY-MM-DD')
      }));
    }
  }
  return function(dispatch) {
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
      success: function(data, status, jqXHR) {
        dispatch(submitRoll(rolls));
        dispatch(reset('rollSlipForm'));
        dispatch(deselectAllEvents());
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('Roll post error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}

export const UPDATE_ROLL_FORM = 'UPDATE_ROLL_FORM'
export const updateRollForm = (values) => {
  return {
    type: UPDATE_ROLL_FORM,
    values: values,
  }
}

export const UPDATE_TRAINEE_VIEW = 'UPDATE_TRAINEE_VIEW'
export const updateTraineeView = (trainee) => {
  return {
    type: UPDATE_TRAINEE_VIEW,
    traineeView: trainee
  }
}

export const UPDATE_EVENTS = 'UPDATE_EVENTS'
export const updateEvents = (events) => {
  return {
    type: UPDATE_EVENTS,
    eventsView: events
  }
}

export const UPDATE_ATTENDANCE = 'UPDATE_ATTENDANCE'
export const updateAttendance = (attendance) => {
  return {
    type: UPDATE_ATTENDANCE,
    attendance: attendance
  }
}

export const CHANGE_TRAINEE_VIEW = 'CHANGE_TRAINEE_VIEW'
export const changeTraineeView = (trainee) => {
  return function(dispatch) {
    dispatch(updateTraineeView(trainee))
    $.ajax({
      url: '/api/events',
      type: 'GET',
      data: {
        trainee: trainee.id
      },
      success: function(data, status, xhr) {
        dispatch(deselectAllEvents())
        for(let i = 0; i < data.length; i++){
          data[i].start = data[i]['start_datetime'];
          data[i].end = data[i]['end_datetime'];
        }
        dispatch(updateEvents(data))
      },
      error: function(xhr, status, error) {
        console.log('events error')
        console.log(xhr, status, error);
      }
    })
    $.ajax({
      url: '/api/attendance',
      type: 'GET',
      data: {
        trainee: trainee.id
      },
      success: function(data, status, xhr) {
        // this returns a list of trainees so just grab the first
        dispatch(updateAttendance(data[0]))
      },
      error: function(xhr, status, error) {
        console.log('attendance error')
        console.log(xhr, status, error)
      }
    })
  }
}

export const CHANGE_LEAVESLIP_FORM = 'CHANGE_LEAVESLIP_FORM'
  //values here is all the values of the form
export const changeLeaveSlipForm = (values) => {
  return {
    type: CHANGE_LEAVESLIP_FORM,
    values: values
  }
}
export const CHANGE_GROUPSLIP_FORM = 'CHANGE_GROUPSLIP_FORM'
  //values here is all the values of the form
export const changeGroupSlipForm = (values) => {
  return {
    type: CHANGE_GROUPSLIP_FORM,
    values: values
  }
}



export const SUBMIT_LEAVESLIP = 'SUBMIT_LEAVESLIP'
export const submitLeaveSlip = (slip) => {
  return {
    type: SUBMIT_LEAVESLIP,
    leaveslip: slip
  }
}

export const postLeaveSlip = (values) => {
  let selectedEvents = values.selectedEvents;
  var event_details = [];
  for (var i = 0; i < selectedEvents.length; i++) {
    event_details.push({
      "id": values.selectedEvents[i].id,
      "date": dateFns.format(selectedEvents[i].start, 'YYYY-MM-DD')
    });
  }
  var texted = false;
  if (values.ta_informed.id == "texted") {
    texted = true;
    values.ta_informed.id = false;
  }
  let slipId = null;
  var slip = {
    "id": slipId,
    "type": values.slipType.id,
    "status": "P",
    "TA": values.ta.id,
    "trainee": values.trainee.id,
    "submitted": Date.now(),
    "last_modified": Date.now(),
    "finalized": null,
    "description": "",
    "comments": values.comments,
    "texted": texted,
    "informed": values.ta_informed.id,
    "events": event_details
  };

  var ajaxType = 'POST';
  var ajaxData = JSON.stringify(slip);
  if (slipId) {
    ajaxType = 'PATCH';
    ajaxData = JSON.stringify([slip]);
  }

  return function(dispatch) {
    return $.ajax({
      url: '/api/individualslips/',
      type: ajaxType,
      contentType: 'application/json',
      data: ajaxData,
      success: function(data, status, jqXHR) {
        console.log("returned data", data, status, jqXHR);
        dispatch(submitLeaveSlip(data));
        dispatch(reset('rollSlipForm'));
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('Slip post error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}

//using destroy because delete is an official HTTP action and is used for the thunk
export const DESTROY_LEAVESLIP = 'DESTROY_LEAVESLIP'
export const destroyLeaveSlip = (slip) => {
  return {
    type: DESTROY_LEAVESLIP,
    slip: slip
  }
}

export const deleteLeaveSlip = (slip) => {
  return function(dispatch) {
    dispatch(destroyLeaveSlip(slip));
    return $.ajax({
      url: '/api/individualslips/' + slip.id.toString(),
      type: 'DELETE',
      success: function(data, status, jqXHR) {
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        // dispatch(removeAllSelectedEvents());
        // dispatch(hideAllForms());
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('Slip delete error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}


export const SUBMIT_GROUPSLIP = 'SUBMIT_GROUPSLIP'
export const submitGroupSlip = (gSlip) => {
  return {
    type: SUBMIT_GROUPSLIP,
    groupslip: gSlip,
  }
}

export const postGroupSlip = (gSlip, selectedEvents, slipId) => {
  var tas = initialState.tas;
  var ta_id = null;
  var texted = false;
  if (gSlip.ta_informed.id == "true") {
    ta_id = gSlip.ta.id;
  } else if (gSlip.ta_informed.id == "texted") {
    texted=true;
    gSlip.ta_informed.id = false;
  }

  // Group slips are assigned to a trainee by time range, so cannot skip events in the middle.
  gSlip.start = gSlip.selectedEvents[0].start
  gSlip.end = gSlip.selectedEvents[0].end
  for (var i = 1; i < gSlip.selectedEvents.length; i++) {
    event = gSlip.selectedEvents[i];
    if (event.start < gSlip.start) {
      gSlip.start = event.start;
    }
    if (event.end > gSlip.end) {
      gSlip.end = event.end;
    }
  }
  var trainee_ids = [];
  for (var i = 0; i < gSlip.trainees.length; i++) {
    trainee_ids.push(gSlip.trainees[i].id);
  }
  var slip = {
    "id": slipId,
    "type": gSlip.slipType.id,
    "status": "P",
    "submitted": Date.now(),
    "last_modified": Date.now(),
    "finalized": null,
    "description": "",
    "comments": gSlip.comment,
    "texted": texted,
    "informed": gSlip.ta_informed.id,
    "start": gSlip.start,
    "end": gSlip.end,
    "TA": ta_id,
    "trainee": null,
    "trainees": trainee_ids
  }
  var ajaxType = 'POST';
  if (slipId) {
    ajaxType = 'PUT';
  }

  return function(dispatch, getState) {
    slip.trainee = getState().trainee.id;
    var ajaxData = JSON.stringify(slip);
    if (slipId) {
      ajaxData = JSON.stringify([slip]);
    }
    return $.ajax({
      url: '/api/groupslips/',
      type: ajaxType,
      contentType: 'application/json',
      data: ajaxData,
      success: function(data, status, jqXHR) {
        dispatch(submitGroupSlip(data));
        dispatch(receiveResponse(status));
        dispatch(reset('groupSlipForm'));
        // dispatch(removeAllSelectedEvents());
        // dispatch(hideAllForms());
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('Slip post error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    });
  }
}

export const DESTROY_GROUPSLIP = 'DESTROY_GROUPSLIP'
export const destroyGroupSlip = (slipId) => {
  return {
    type: DESTROY_GROUPSLIP,
    slipId: slipId
  }
}

export const deleteGroupSlip = (slipId) => {
  return function(dispatch) {
    dispatch(destroyGroupSlip(slipId));
    return $.ajax({
      url: '/api/groupslips/' + slipId.toString(),
      type: 'DELETE',
      success: function(data, status, jqXHR) {
        dispatch(receiveResponse(status));
        dispatch(reset('rollSlipForm'));
        // dispatch(removeAllSelectedEvents());
        // dispatch(hideAllForms());
      },
      error: function(jqXHR, textStatus, errorThrown) {
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

export const SELECT_TAB = 'SELECT_TAB'
export const selectTab = (index, trainee) => {
  return function(dispatch) {
    dispatch(showCalendar(index))
    dispatch(changeTraineeView(trainee))
  }
}

export const SHOW_CALENDAR = 'SHOW_CALENDAR'
export const showCalendar = (index) => {
  switch (index) {
    case 1:
      return {
        type: SHOW_CALENDAR,
        value: 'summary'
      }
    case 2:
      return {
        type: SHOW_CALENDAR,
        value: 'roll'
      }
    case 3:
      return {
        type: SHOW_CALENDAR,
        value: 'leaveslip'
      }
    case 4:
      return {
        type: SHOW_CALENDAR,
        value: 'groupslip'
      }
  }
}

export const SELECT_GROUPSLIP = 'SELECT_GROUPSLIP'
export const selectGroupslip = (id) => {
  return {
    type: SELECT_GROUPSLIP,
    id: id
  }
}

export const SELECT_LEAVESLIP = 'SELECT_LEAVESLIP'
export const selectLeaveslip = (id) => {
  return {
    type: SELECT_LEAVESLIP,
    id: id
  }
}

export const SELECT_EVENT = 'SELECT_EVENT'
export const selectEvent = (id) => {
  return {
    type: SELECT_LEAVESLIP,
    id: id
  }
}
