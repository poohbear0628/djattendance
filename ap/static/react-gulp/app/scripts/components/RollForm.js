import React, { Component, PropTypes } from 'react'
import { Button } from 'react-bootstrap'
import { reduxForm } from 'redux-form'
export const fields = [ 'rollStatus' ]

//forms use the redux-form library
//http://redux-form.com/
const RollForm =({fields: { rollStatus }, handleSubmit, resetForm, submitting}) => {

  return (
    <form onSubmit={handleSubmit}>
      <div style={{width: "100%", paddingBottom: "30px"}} data-toggle="buttons">
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="Present" checked={rollStatus.value === "Present"} name="options" /> Present
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="Absent" checked={rollStatus.value === "Absent"} name="options" /> Absent
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="Tardy" checked={rollStatus.value === "Tardy"} name="options" /> Tardy
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="Uniform" checked={rollStatus.value === "Uniform"} name="options" /> Uniform
        </label>
        <label className="roll-input">
          <input type="radio" {...rollStatus} value="Left Class" checked={rollStatus.value === "Left Class"} name="options" /> Left Class
        </label>
      </div>
      <div className="form-buttons">
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
  submitting: PropTypes.bool.isRequired
}

export default reduxForm({
  form: 'rollForm',
  fields
})(RollForm)
