import React, { Component, PropTypes } from 'react'
import { Button, Alert } from 'react-bootstrap'
import Form from 'react-formal'
import types from 'react-formal-inputs'
import yup from 'yup'

import { SLIP_TYPES, INFORMED, SLIP_TYPE_LOOKUP, TA_IS_INFORMED } from '../constants'

//gives us advanced form inputs like selectlist - see
//https://github.com/jquense/react-formal-inputs
//http://jquense.github.io/react-widgets/docs/
Form.addInputTypes(types)

//lets use yup to do client side validation!
let modelSchema = (props) => {
  let nightFieldSchema = yup.mixed().when('slipType', {
    is: (val) => {
      return val.id == 'NIGHT'
    },
    then: yup.string().required('Please fill in all the fields for night/meal out'),
  })
  let mealFieldSchema = yup.mixed().when('slipType', {
    is: (val) => {
      return val.id == 'MEAL' || val.name == 'NIGHT'
    },
    then: yup.string().required('Please fill in all the fields for night/meal out'),
  })
  return yup.object({
    selectedEvents: yup.array().required("Please select an event"),
    trainee: yup.object().required("If you see this, something is wrong."),
    slipType: yup.mixed().notOneOf([''], "Please select a reason for your leaveslip"),
    ta_informed: yup.object(),
    ta: yup.mixed().when('ta_informed', {
      is: (val) => {
        return val.id == TA_IS_INFORMED.id
      },
      then: yup.mixed().notOneOf([''], "Please select a TA." )
    }),
    comment: yup.string(),

    location: mealFieldSchema,
    hostName: mealFieldSchema,
    hostPhone: nightFieldSchema,
    hcNotified: nightFieldSchema,
  });
}

//comments - with react-dev-tools on, this is really slow. However, it works fine when react dev tool is disabled.
const LeaveSlipForm = ({...props}) => {

  let slipTypes = SLIP_TYPES
  let addLastSlips = (slips) => {
    let slipIds = slips.map((s) => s.type)
    let dates = slips.map((s) => s.events.slice(-1)[0].date)
    slipTypes = SLIP_TYPES.map((s) => {
      let slip = _.clone(s)
      let index = slipIds.indexOf(slip.id)
      if (index >= 0) {
        slip.name += ' (last slip: ' + dates[index] + ')'
      }
      return slip
    })
  }
  addLastSlips(props.lastSlips)

  let schema = modelSchema(props);
  return (
    <div className='dt-leaveslip'>
    <Form
      schema={schema}
      value={props.form}
      onChange={(values) => { //console.log(values);
        props.changeLeaveSlipForm(values) }}
      onSubmit={props.postLeaveSlip}
    >

      <h4 className='dt-leaveslip__title'>Submit Leaveslip</h4>
      <b>Selected Events</b>
      <Form.Field type='multiSelect' open={false} name='selectedEvents' valueField='id' textField='code' className='dt-leaveslip__multi' />
      <b>Reason</b>
      <Form.Field type='dropdownList' placeholder='Choose a reason' data={slipTypes} name='slipType' valueField='id' textField='name' />

      {
        (props.form.slipType.id == 'MEAL' || props.form.slipType.id == 'NIGHT') &&
        <div>
          <b>Location (address for night out)</b>
          <Form.Field type="textarea" name="location" className="dt-leaveslip__location"/>
          <b>Host name</b>
          <Form.Field name="hostName" className="dt-leaveslip__host-name"/>
        </div>
      }

      {
        props.form.slipType.id == 'NIGHT' &&
        <div>
          <b>Host phone number</b>
          <Form.Field name="hostPhone" className="dt-leaveslip__host-phone"/>
          <b>HC Notified</b>
          <Form.Field name="hcNotified" className="dt-leaveslip__hc-notified" />
        </div>
      }

      <h4 className='dt-leaveslip__title'>Comments</h4>
      <Form.Field type='textarea' name='comment' events={['onBlur']} className='dt-leaveslip__comments'/>

      <h4 className='dt-leaveslip__title'>TA informed (if any)</h4>
      <Form.Field type='dropdownList' name='ta_informed' className="dt-leaveslip__ta-informed" data={INFORMED} valueField='id' textField='name' />
      {
        props.form.ta_informed.id == TA_IS_INFORMED.id &&
        <Form.Field type='dropdownList' data={props.tas} name='ta' placeholder='Choose a TA' className="dt-leaveslip__ta-list" valueField='id' textField='name' />
      }

      <Form.Summary className="alert alert-danger"/>
      <Alert bsStyle="warning" className="dt-leaveslip__note">
        <b>Meal sign out:</b> If your leave of absence permits you to miss a meal, <u>you must also</u> sign out on the appropriate meal sign-out sheet.
        <br/>
        <br/>
        <b>Service scheduling:</b> If your leave of absence permits you to be out of the schedule for seven days or more, <u>you must also</u> submit a note to the service scheduling mail slot.
      </Alert>
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
