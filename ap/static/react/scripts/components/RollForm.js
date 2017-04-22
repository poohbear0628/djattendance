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
  let traineeField = '';
  if (props.form.trainee.groups.indexOf(ATTENDANCE_MONITOR_GROUP) >= 0) {
    traineeField = <div>
      <b>Trainee</b>
      <Select name="traineeView" clearable={false} options={props.form.trainees} labelKey='name' valueKey='id' value={props.form.traineeView} onChange={props.changeTraineeView} />
    </div>
  }
  return (
    <div className='dt-roll'>
      <h4>Submit Roll</h4>
      <Form
        schema={schema}
        onChange={props.updateRollForm}
        onSubmit={props.postRoll}
      >
        <b>Selected Events</b>
        {/* open={false} gives a warning but readOnly and disabled don't work satisfactorily */}
        <Form.Field type='multiSelect' open={false} data={props.form.selectedEvents} name='selectedEvents' valueField='id' textField='code' className='dt-roll__multi' />
        <b>Reason</b>
        <Form.Field type='selectList' data={ATTENDANCE_STATUS} name='rollStatus' valueField='id' textField='name' />
        {traineeField}
        <Form.Message for='rollStatus'/>
        <Form.Message for='selectedEvents'/>
        <Form.Button className='dt-submit' type='submit'>Submit Roll</Form.Button>
        <Form.Button className='dt-submit' type='button' disabled={!props.canFinalizeWeek} onClick={props.finalizeRoll} >Finalize Roll</Form.Button>
      </Form>
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
