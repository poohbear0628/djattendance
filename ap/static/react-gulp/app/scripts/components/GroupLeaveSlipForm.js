import React, { Component, PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import { reduxForm } from 'redux-form'
import initialState from '../initialState'
import { postLeaveSlip } from '../actions'
import TraineeSelect from './TraineeSelect'

import Select from 'react-select'

export const fields = [ 'trainees', 'slipType', 'comments', 'informed', 'TAInformed' ]

const validate = (values, props) => {
  var ta_names = [];
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    ta_names.push(initialState.reducer.tas[i].firstname + ' ' + initialState.reducer.tas[i].lastname);
  }
  const errors = {}
  if (props.submitLeaveSlipShow && values.informed == "true" && !ta_names.includes(values.TAInformed)) {
    errors.TAInformed = 'No TA selected';
  }
  if (props.submitLeaveSlipShow && !values.slipType) {
    console.log('slipType error');
    errors.slipType = 'No reason selected';
  } 
  return errors
}

//forms use the redux-form library
//http://redux-form.com/
const GroupLeaveSlipForm = ({fields: { trainees, slipType, comments, informed, TAInformed }, handleSubmit, resetForm, 
                    submitGroupLeaveSlipShow, otherReasonsShow, toggleSubmitGroupLeaveSlip, toggleOtherReasons,
                    submitting, post, tas, selectedEvents, traineeSelectOptions}) => {

  return (
    <form onSubmit={handleSubmit(post)}>
      <div className="position-container">
        <Collapse in={submitGroupLeaveSlipShow}>
          <div className="form-body">
            <div className="form-section">
              <TraineeSelect {...trainees} options={traineeSelectOptions}/>
              <div className="toggle-title">Reason</div>
              <div>
                <div className="reason-container">
                  <label className="radio-input">
                    <input type="radio" {...slipType} name="reason" value="FWSHP" checked={slipType.value === "FWSHP"}/> Fellowship 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipType} name="reason" value="SERV" checked={slipType.value === "SERV"}/> Service 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipType} name="reason" value="CONF" checked={slipType.value === "CONF"}/> Conference 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipType} name="reason" value="GOSP" checked={slipType.value === "GOSP"}/> Gospel 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipType} name="reason" value="NIGHT" checked={slipType.value === "NIGHT"}/> Night Out 
                  </label>
                  <span onClick={toggleOtherReasons} className="checkbox-container">
                    <input type="checkbox" checked={otherReasonsShow}/> More <span className="caret"></span>
                  </span>
                  <Collapse in={otherReasonsShow}>
                    <div>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="SICK" checked={slipType.value === "SICK"}/> Sickness 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="MEAL" checked={slipType.value === "MEAL"}/> Meal Out 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="INTVW" checked={slipType.value === "INTVW"}/> Interview 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="WED" checked={slipType.value === "WED"}/> Wedding 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="FUNRL" checked={slipType.value === "FUNRL"}/> Funeral 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipType} name="reason" value="SPECL" checked={slipType.value === "SPECL"}/> Special 
                      </label>
                      <label className="radio-input" style={{width: "33%"}}>
                        <input type="radio" {...slipType} name="reason" value="OTHER" checked={slipType.value === "OTHER"}/> Other 
                      </label>
                      <label className="radio-input" style={{width: "66%"}}>
                        <input type="radio" {...slipType} name="reason" value="EMERG" checked={slipType.value === "EMERG"}/> Family Emergency 
                      </label>
                    </div>
                  </Collapse>
                </div>
                <div className="border-top">
                  <label className="notification-only">
                    <input type="radio" {...slipType} name="reason" value="NOTIF" checked={slipType.value === "NOTIF"}/> Notification Only 
                  </label>
                </div>
                {slipType.touched && slipType.error && <div className="form-error">{slipType.error}</div>}
              </div>
              <div>
                <div className="toggle-title">Comments</div>
                <textarea className="comments-textarea"
                  {...comments}
                  defaultValue={comments.value || ''}
                />
              </div>
              <div className="position-container">
                <select className="form-control select-inform-status" {...informed} value={informed.value || ''}>
                  <option value={true}>TA informed </option>
                  <option value={false}>Did not inform training office </option>
                  <option value="texted">Texted attendance number (for sisters during non-front office hours only)</option>
                </select>
                <span className="caret select-caret"></span>
              </div>
              <Collapse in={informed.value == "true"}>
                <div className="ta-names">
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Andrew Li" checked={TAInformed.value === "Andrew Li"}/> Andrew Li 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Jerome Keh" checked={TAInformed.value === "Jerome Keh"}/> Jerome Keh 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Joseph Bang" checked={TAInformed.value === "Joseph Bang"}/> Joseph Bang
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Paul Deng" checked={TAInformed.value === "Paul Deng"}/> Paul Deng 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Walt Hale" checked={TAInformed.value === "Walt Hale"}/> Walt Hale 
                  </label>
                </div>
              </Collapse>
              {TAInformed.touched && TAInformed.error && <div className="form-error">{TAInformed.error}</div>}
            </div>
          </div>
        </Collapse>
        <Collapse in={submitGroupLeaveSlipShow}>
          <div className="form-buttons">
            <Button type="button" disabled={submitting} onClick={resetForm} bsSize="xsmall" style={{marginRight: "3px"}}>
              Clear Values
            </Button>
            <Button type="submit" disabled={submitting || TAInformed.error || slipType.error} bsStyle="primary" bsSize="xsmall">
              {submitting ? <i/> : <i/>} Submit
            </Button>
          </div>
        </Collapse>
      </div>
    </form>
  )
}


GroupLeaveSlipForm.propTypes = {
  fields: PropTypes.object.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  resetForm: PropTypes.func.isRequired,
  submitting: PropTypes.bool.isRequired,
  post: PropTypes.func.isRequired,
  toggleOtherReasons: PropTypes.func.isRequired
}

export default reduxForm({
  form: 'groupLeaveSlipForm',
  fields,
  validate
})(GroupLeaveSlipForm)
