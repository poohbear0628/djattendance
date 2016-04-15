import React, { Component, PropTypes } from 'react'
import { Button } from 'react-bootstrap'
import { reduxForm } from 'redux-form'
export const fields = [ 'rollStatus' ]

//forms use the redux-form library
//http://redux-form.com/
const RollForm =({fields: { rollStatus }, handleSubmit, resetForm, submitting, post, submitLeaveSlipShow}) => {
  var hideButtons = {};
  if (submitLeaveSlipShow) {
    hideButtons = {display: "none"};
  }
  return (
    <form onSubmit={handleSubmit(post)}>
      <div style={{width: "100%", paddingBottom: "30px"}} data-toggle="buttons">
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="P" checked={rollStatus.value === "P"} name="options" /> Present
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="A" checked={rollStatus.value === "A"} name="options" /> Absent
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="T" checked={rollStatus.value === "T"} name="options" /> Tardy
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="U" checked={rollStatus.value === "U"} name="options" /> Uniform
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="L" checked={rollStatus.value === "L"} name="options" /> Left Class
        </label>
      </div>
      <div className="form-buttons" style={hideButtons}>
        <Button type="button" disabled={submitting} onClick={resetForm} bsSize="xsmall" style={{marginRight: "3px"}}>
          Clear Values
        </Button>
        <Button type="submit" disabled={submitting} bsStyle="primary" bsSize="xsmall">
          {submitting ? <i/> : <i/>} Submit
        </Button>
      </div>
    </form>
  )
}


RollForm.propTypes = {
  fields: PropTypes.object.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  resetForm: PropTypes.func.isRequired,
  submitting: PropTypes.bool.isRequired,
  post: PropTypes.func.isRequired
}

export default reduxForm({
  form: 'rollForm',
  fields
})(RollForm)
