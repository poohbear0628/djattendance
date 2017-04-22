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
    trainee: yup.object().required("If you see this, something is wrong."),
    trainees: yup.array().required("Please select some trainees"),
    slipType: yup.object().required("Please select a reason for your groupslip"),
    ta_informed: yup.object(),
    ta: yup.object(),
    comment: yup.string(),
    selectedEvents: yup.array().required("Please select an event"),
  });
}

//comments - with react-dev-tools on, this is really slow. However, it works fine when react dev tool is disabled.
const GroupSlipForm = ({...props}) => {
  let schema = modelSchema(props);
  let selectTA = props.form.ta_informed['id'] == 'true' ? <div className="dt-leaveslip__ta">
      <Form.Field type='selectList' data={props.tas} name='ta' valueField='id' textField='name' />
      </div> : '';
  //onchange is written so you can console.log if you need to test things
  //onsubmit is shorthand equivalent of onchange
  return (
    <div className="dt-leaveslip">
      <h4 className='dt-leaveslip__title'>Submit GroupSlip</h4>
      <Form
        schema={schema}
        value={props.form}
        onChange={(values) => {console.log(values);props.changeGroupSlipForm(values) }}
        onSubmit={props.postGroupSlip}
      >
        <b>Select Trainees</b>
        <Form.Field type='multiSelect' data={props.trainees} name='trainees' valueField='id' textField='name' className='dt-leaveslip__multi' />
        <b>Selected Events</b>
        <Form.Field type='multiSelect' name='selectedEvents' valueField='id' textField='code' className='dt-leaveslip__selectedEvents' />
        <Form.Field type='selectList' data={SLIP_TYPES} name='slipType' valueField='id' textField='name' />
        <h4 className='dt-leaveslip__title'>Comments</h4>
        <Form.Field type='textarea' name='comment' events={['onBlur']} className='dt-leaveslip__comments'/>
        <b>TA Form</b>
        <Form.Field type='dropdownList' name='ta_informed' className="dt-leaveslip__ta-informed" data={INFORMED} valueField='id' textField='name' />

        {selectTA}

        <Form.Summary />
        <Form.Button className='dt-submit' type='submit'>Submit GroupSlip</Form.Button>
      </Form>
    </div>
  )
}


GroupSlipForm.propTypes = {
  // fields: PropTypes.object.isRequired,
  // handleSubmit: PropTypes.func.isRequired,
  // resetForm: PropTypes.func.isRequired,
  // submitting: PropTypes.bool.isRequired,
  // post: PropTypes.func.isRequired,
  // toggleOtherReasons: PropTypes.func.isRequired
}
export default GroupSlipForm;
