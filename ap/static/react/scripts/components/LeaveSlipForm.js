import React, { Component, PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import Form from 'react-formal'
import types from 'react-formal-inputs'
import yup from 'yup'
import { SLIP_TYPES, INFORMED } from '../constants'

//gives us advanced form inputs like selectlist - see
//https://github.com/jquense/react-formal-inputs
//http://jquense.github.io/react-widgets/docs/
Form.addInputTypes(types)

//lets use yup to do client side validation!
let modelSchema = (props) => {
  return yup.object({
    selectedEvents: yup.array().required("Please select an event"),
    trainee: yup.object().required("If you see this, something is wrong."),
    slipType: yup.mixed().notOneOf([{}], "Please select a reason for your leaveslip"),
    ta_informed: yup.string(),
    ta: yup.mixed().when('ta_informed', {
      is: 'true',
      then: yup.mixed().notOneOf([{}], "Please select a TA." )
    }),
    comment: yup.string(),
  });
}

//comments - with react-dev-tools on, this is really slow. However, it works fine when react dev tool is disabled.
const LeaveSlipForm = ({...props}) => {
  let schema = modelSchema(props);
  let selectTA = props.form.ta_informed.id == 'true' ? <div className="dt-leaveslip__ta">
      <Form.Field type='selectList' data={props.tas} name='ta' valueField='id' textField='firstname' />
      </div> : '';
  return (
    <div className='dt-leaveslip'>
    <h4 className='dt-leaveslip__title'>Submit Leaveslip</h4>
    <Form
      schema={schema}
      value={props.form}
      onChange={(values) => { //console.log(values);
        props.changeLeaveSlipForm(values) }}
      onSubmit={props.postLeaveSlip}
    >
      <b>Selected Events</b>
      <Form.Field type='multiSelect' data={props.selectedEvents} name='selectedEvents' valueField='id' textField='code' className='dt-leaveslip__multi' />
      <b>Reason</b>
      <Form.Field type='selectList' data={SLIP_TYPES} name='slipType' valueField='id' textField='name' />
      <h4 className='dt-leaveslip__title'>Comments</h4>
      <Form.Field type='textarea' name='comment' events={['onBlur']} className='dt-leaveslip__comments'/>
      <div>
        <Form.Field type='dropdownList' name='ta_informed' className="dt-leaveslip__ta-informed" data={INFORMED} valueField='id' textField='name' />
        {selectTA}
      </div>

      <Form.Summary />
      <Form.Button className='dt-submit' type='submit'>Submit Leaveslip</Form.Button>
    </Form>
    </div>
  )
}

LeaveSlipForm.propTypes = {
  // fields: PropTypes.object.isRequired,
  // handleSubmit: PropTypes.func.isRequired,
  // resetForm: PropTypes.func.isRequired,
  // submitting: PropTypes.bool.isRequired,
  // post: PropTypes.func.isRequired,
  // toggleOtherReasons: PropTypes.func.isRequired
}
export default LeaveSlipForm;
