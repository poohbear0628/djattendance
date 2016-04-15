import React, { Component, PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import { reduxForm } from 'redux-form'
import initialState from '../initialState'
import { postLeaveSlip } from '../actions'
export const fields = [ 'slipReason', 'comments', 'informStatus', 'TAInformed', 'selectedEvents' ]

const submit = (values, dispatch) => {
  var ta_names = [];
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    ta_names.push(initialState.reducer.tas[i].firstname + ' ' + initialState.reducer.tas[i].lastname);
  }
  console.log(values);
  return new Promise((resolve, reject) => {
    if (!ta_names.includes(values.TAInformed)) {
      reject({ TAInformed: 'TA does not exist', _error: 'No TA selected!' });
    } else if (!values.slipReason) {
      reject({ password: 'No reason selected', _error: 'No reason selected!' });
    } else {
      dispatch(postLeaveSlip(values));
      resolve()
    }
  })
}

//forms use the redux-form library
//http://redux-form.com/
const SlipForm = ({fields: { slipReason, comments, informStatus, TAInformed, selectedEvents }, handleSubmit, resetForm, 
                    submitting, post, toggleOtherReasons, otherReasonsShow, tas}) => {
  var selectStyle = {
    width: "42%",
    transition: "width 1s"
  };
  var inputStyle = {
    width: "58%", 
    visibility: "visible", 
    borderBottomRightRadius: "3px",
    borderTopRightRadius: "3px",
    borderBottomLeftRadius: "0",
    borderTopLeftRadius: "0",
    transition: "width 1s, visibility 1s, padding 2s, border 2s"
  };
  var caretStyle = {
    position: "absolute",
    zIndex: 5,
    top: "15px",
    left: "-20px",
    transition: "left 1s"
  };

  if (informStatus.value == "false") {
    selectStyle = {
      width: "100%",
      borderRadius: "3px",
      transition: "width 1s"
    };
    inputStyle = {
      width: "0%",
      padding: 0,
      border: 0,
      visibility: "hidden",
      transition: "width 1s, visibility 0s"
    };
    caretStyle = {
      position: "absolute",
      zIndex: 5,
      top: "15px",
      left: "-20px",
      transition: "left 1s"
    }
  }

  var errorStyle = {}
  if (TAInformed.touched && TAInformed.error) {
    errorStyle = {
      color: "#a94442",
      borderColor: "#a94442"
    }
  }

  return (
    <form onSubmit={handleSubmit(submit)}>
      <div className="toggle-title">Reason</div>
      <div data-toggle="buttons">
        <div className="reason-container">
          <label className="roll-input">
            <input type="radio" {...slipReason} name="options" value="SICK" checked={slipReason.value === "SICK"}/> Sickness 
          </label>
          <label className="roll-input">
            <input type="radio" {...slipReason} name="options" value="SERV" checked={slipReason.value === "SERV"}/> Service 
          </label>
          <label className="roll-input">
            <input type="radio" {...slipReason} name="options" value="FWSHP" checked={slipReason.value === "FWSHP"}/> Fellowship 
          </label>
          <label className="roll-input">
            <input type="radio" {...slipReason} name="options" value="NIGHT" checked={slipReason.value === "NIGHT"}/> Night Out 
          </label>
          <label className="roll-input">
            <input type="radio" {...slipReason} name="options" value="MEAL" checked={slipReason.value === "MEAL"}/> Meal Out 
          </label>
          <span onClick={toggleOtherReasons} className="checkbox-container">
            <input type="checkbox" checked={otherReasonsShow}/> More <span className="caret"></span>
          </span>
          <Collapse in={otherReasonsShow}>
            <div data-toggle="buttons">
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="INTVW" checked={slipReason.value === "INTVW"}/> Interview 
              </label>
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="GOSP" checked={slipReason.value === "GOSP"}/> Gospel 
              </label>
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="CONF" checked={slipReason.value === "CONF"}/> Conference 
              </label>
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="WED" checked={slipReason.value === "WED"}/> Wedding 
              </label>
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="FUNRL" checked={slipReason.value === "FUNRL"}/> Funeral 
              </label>
              <label className="roll-input">
                <input type="radio" {...slipReason} name="options" value="SPECL" checked={slipReason.value === "SPECL"}/> Special 
              </label>
              <label className="roll-input" style={{width: "33%"}}>
                <input type="radio" {...slipReason} name="options" value="OTHER" checked={slipReason.value === "OTHER"}/> Other 
              </label>
              <label className="roll-input" style={{width: "66%"}}>
                <input type="radio" {...slipReason} name="options" value="EMERG" checked={slipReason.value === "EMERG"}/> Family Emergency 
              </label>
            </div>
          </Collapse>
        </div>
        <div className="border-top">
          <label className="notification-only">
            <input type="radio" {...slipReason} name="options" value="NOTIF" checked={slipReason.value === "NOTIF"}/> Notification Only 
          </label>
        </div>
        {slipReason.touched && slipReason.error && <div style={errorStyle}>{slipReason.error}</div>}
      </div>
      <div>
        <div className="toggle-title">Comments</div>
        <textarea className="comments-textarea"
          {...comments}
          value={comments.value || ''}
        />
      </div>
      <div className="input-group" style={{width: "100%"}}>
        <select className="form-control select-inform-status" style={selectStyle}
          {...informStatus}
          value={informStatus.value || ''}>
          <option selected="selected" value={true}>TA informed </option>
          <option value={false}>Did not inform training office </option>
        </select>
        <span style={{position: "relative"}}>
          <span className="caret" style={caretStyle}></span>
          <input type="text" className="form-control awesomplete" style={Object.assign(inputStyle, errorStyle)}
            {...TAInformed} data-list={tas.toString()} data-minchars="1" data-autofirst="true"/>
        </span>
      </div>
      {TAInformed.touched && TAInformed.error && <div style={errorStyle}>{TAInformed.error}</div>}
      <div className="form-buttons">
        <Button type="button" disabled={submitting} onClick={resetForm} bsSize="xsmall" style={{marginRight: "3px"}}>
          Clear Values
        </Button>
        <Button type="submit" disabled={submitting || TAInformed.error} bsStyle="primary" bsSize="xsmall">
          {submitting ? <i/> : <i/>} Submit
        </Button>
      </div>
    </form>
  )
}


SlipForm.propTypes = {
  fields: PropTypes.object.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  resetForm: PropTypes.func.isRequired,
  submitting: PropTypes.bool.isRequired,
  post: PropTypes.func.isRequired,
  toggleOtherReasons: PropTypes.func.isRequired
}

export default reduxForm({
  form: 'slipForm',
  fields
})(SlipForm)
