import React, { Component, PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import Select from 'react-select';
import Form from 'react-formal'
import types from 'react-formal-inputs'
import yup from 'yup'

import { ATTENDANCE_STATUS, ATTENDANCE_MONITOR_GROUP } from '../constants'

//gives us advanced form inputs like selectlist - see
//https://github.com/jquense/react-formal-inputs
//http://jquense.github.io/react-widgets/docs/
Form.addInputTypes(types)

//lets use yup to do client side validation!
let modelSchema = (props) => {
  return yup.object({
    rollStatus: yup.object().required("Please select a roll"),
    selectedEvents: yup.array().required("Please select an event"),
    traineeView: yup.object().required("If you see this, something is wrong."),
  });
}

const RollForm = ({...props}) => {
  let schema = modelSchema(props);
  return (
    <div className='dt-roll'>
      <h4>Submit Roll</h4>
      <Form
        schema={schema}
        value={props.form}
        onChange={props.updateRollForm}
        onSubmit={props.postRoll}
      >
        <b>Selected Events</b>
        <Form.Field type='multiSelect' open={false} name='selectedEvents' valueField='id' textField='code' className='dt-roll__multi' />
        <b>Reason</b>
        <Form.Field type='selectList' data={ATTENDANCE_STATUS} name='rollStatus' valueField='id' textField='name' />
        {
          props.form.trainee.groups.indexOf(ATTENDANCE_MONITOR_GROUP) >= 0 &&
          <div className="dt-roll__trainee-select">
            <b>Trainee</b>
            <Select name="traineeView" clearable={false} options={props.form.trainees} labelKey='name' valueKey='id' value={props.form.traineeView} onChange={props.changeTraineeView} />
          </div>
        }
        <Form.Message for='rollStatus'/>
        <Form.Message for='selectedEvents'/>
        <Form.Button className='dt-submit' type='submit' disabled={!props.canSubmitRoll}>Submit Roll</Form.Button>
      </Form>
      <Form.Button className='dt-submit' type='button' disabled={!props.canFinalizeWeek} onClick={props.finalizeRoll} >Finalize Roll</Form.Button>
    </div>
  )
}


RollForm.propTypes = {
  // fields: PropTypes.object.isRequired,
  // handleSubmit: PropTypes.func.isRequired,
  // resetForm: PropTypes.func.isRequired,
  // submitting: PropTypes.bool.isRequired,
  // post: PropTypes.func.isRequired,
  // toggleOtherReasons: PropTypes.func.isRequired
}
export default RollForm;
