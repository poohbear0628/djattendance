import React, { Component, PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import { reduxForm } from 'redux-form'
import initialState from '../initialState'
import { postLeaveSlip } from '../actions'
export const fields = [ 'rollStatus', 'slipReason', 'comments', 'informStatus', 'TAInformed' ]

const validate = (values, props) => {
  var ta_names = [];
  for (var i = 0; i < initialState.reducer.tas.length; i++) {
    ta_names.push(initialState.reducer.tas[i].firstname + ' ' + initialState.reducer.tas[i].lastname);
  }
  console.log('values: ', values);
  console.log(values.slipReason, !values.slipReason);
  console.log('props: ', props);
  const errors = {}
  if (props.submitLeaveSlipShow && values.informStatus == "true" && !ta_names.includes(values.TAInformed)) {
    errors.TAInformed = 'No TA selected';
  }
  if (props.submitLeaveSlipShow && !values.slipReason) {
    console.log('slipReason error');
    errors.slipReason = 'No reason selected';
  } 
  return errors
}

//forms use the redux-form library
//http://redux-form.com/
const RollSlipForm = ({fields: { rollStatus, slipReason, comments, informStatus, TAInformed }, handleSubmit, resetForm, 
                    submitRollShow, submitLeaveSlipShow, otherReasonsShow, toggleSubmitLeaveSlip, toggleOtherReasons,
                    submitting, post, tas, selectedEvents}) => {
  var errorStyle = {}
  if (TAInformed.touched && TAInformed.error) {
    errorStyle = {
      color: "#a94442",
      borderColor: "#a94442"
    }
  }

  return (
    <form onSubmit={handleSubmit(post)}>
      <div className="position-container">
        <Collapse in={submitRollShow}>
          <div className="form-body form-together">
            <div className="form-section">
              <div className="toggle-title">Enter Roll</div>
              <div style={{width: "100%", paddingBottom: "30px"}} data-toggle="buttons">
                <label className="radio-input">
                  <input type="radio" {...rollStatus} value="P" checked={rollStatus.value === "P"} name="status" /> Present
                </label>
                <label className="radio-input">
                  <input type="radio" {...rollStatus} value="A" checked={rollStatus.value === "A"} name="status" /> Absent
                </label>
                <label className="radio-input">
                  <input type="radio" {...rollStatus} value="T" checked={rollStatus.value === "T"} name="status" /> Tardy
                </label>
                <label className="radio-input">
                  <input type="radio" {...rollStatus} value="U" checked={rollStatus.value === "U"} name="status" /> Uniform
                </label>
                <label className="radio-input">
                  <input type="radio" {...rollStatus} value="L" checked={rollStatus.value === "L"} name="status" /> Left Class
                </label>
              </div>
              <div onClick={toggleSubmitLeaveSlip} className="checkbox-container leaveslip-checkbox">
                <input type="checkbox" checked={submitLeaveSlipShow}/> Leave Slip
              </div>
            </div>
          </div>
        </Collapse>
        <Collapse in={submitLeaveSlipShow}>
          <div className="form-body form-together">
            <div className="form-section">
              <div className="toggle-title">Reason</div>
              <div data-toggle="buttons">
                <div className="reason-container">
                  <label className="radio-input">
                    <input type="radio" {...slipReason} name="reason" value="SICK" checked={slipReason.value === "SICK"}/> Sickness 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipReason} name="reason" value="SERV" checked={slipReason.value === "SERV"}/> Service 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipReason} name="reason" value="FWSHP" checked={slipReason.value === "FWSHP"}/> Fellowship 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipReason} name="reason" value="NIGHT" checked={slipReason.value === "NIGHT"}/> Night Out 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...slipReason} name="reason" value="MEAL" checked={slipReason.value === "MEAL"}/> Meal Out 
                  </label>
                  <span onClick={toggleOtherReasons} className="checkbox-container">
                    <input type="checkbox" checked={otherReasonsShow}/> More <span className="caret"></span>
                  </span>
                  <Collapse in={otherReasonsShow}>
                    <div data-toggle="buttons">
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="INTVW" checked={slipReason.value === "INTVW"}/> Interview 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="GOSP" checked={slipReason.value === "GOSP"}/> Gospel 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="CONF" checked={slipReason.value === "CONF"}/> Conference 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="WED" checked={slipReason.value === "WED"}/> Wedding 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="FUNRL" checked={slipReason.value === "FUNRL"}/> Funeral 
                      </label>
                      <label className="radio-input">
                        <input type="radio" {...slipReason} name="reason" value="SPECL" checked={slipReason.value === "SPECL"}/> Special 
                      </label>
                      <label className="radio-input" style={{width: "33%"}}>
                        <input type="radio" {...slipReason} name="reason" value="OTHER" checked={slipReason.value === "OTHER"}/> Other 
                      </label>
                      <label className="radio-input" style={{width: "66%"}}>
                        <input type="radio" {...slipReason} name="reason" value="EMERG" checked={slipReason.value === "EMERG"}/> Family Emergency 
                      </label>
                    </div>
                  </Collapse>
                </div>
                <div className="border-top">
                  <label className="notification-only">
                    <input type="radio" {...slipReason} name="reason" value="NOTIF" checked={slipReason.value === "NOTIF"}/> Notification Only 
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
              <div className="position-container">
                <select className="form-control select-inform-status" {...informStatus} value={informStatus.value || ''}>
                  <option value={true}>TA informed </option>
                  <option value={false}>Did not inform training office </option>
                  <option value="texted">Texted attendance number (for sisters during non-front office hours only)</option>
                </select>
                <span className="caret select-caret"></span>
              </div>
              <Collapse in={informStatus.value == "true"}>
                <div className="ta-names">
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Andrew Li" checked={TAInformed.value === "Andrew Li"}/> Andrew Li 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Jerome Keh" checked={TAInformed.value === "Jerome Keh"}/> Jerome Keh 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Joe Prim" checked={TAInformed.value === "Joe Prim"}/> Joe Prim
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Paul Deng" checked={TAInformed.value === "Paul Deng"}/> Paul Deng 
                  </label>
                  <label className="radio-input">
                    <input type="radio" {...TAInformed} name="ta" value="Walt Hale" checked={TAInformed.value === "Walt Hale"}/> Walt Hale 
                  </label>
                </div>
              </Collapse>
              {TAInformed.touched && TAInformed.error && <div style={errorStyle}>{TAInformed.error}</div>}
            </div>
          </div>
        </Collapse>
        <Collapse in={submitRollShow || submitLeaveSlipShow}>
          <div className="form-buttons">
            <Button type="button" disabled={submitting} onClick={resetForm} bsSize="xsmall" style={{marginRight: "3px"}}>
              Clear Values
            </Button>
            <Button type="submit" disabled={submitting || TAInformed.error || slipReason.error} bsStyle="primary" bsSize="xsmall">
              {submitting ? <i/> : <i/>} Submit
            </Button>
          </div>
        </Collapse>
      </div>
    </form>
  )
}


RollSlipForm.propTypes = {
  fields: PropTypes.object.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  resetForm: PropTypes.func.isRequired,
  submitting: PropTypes.bool.isRequired,
  post: PropTypes.func.isRequired,
  toggleOtherReasons: PropTypes.func.isRequired
}

export default reduxForm({
  form: 'rollSlipForm',
  fields,
  validate
})(RollSlipForm)
