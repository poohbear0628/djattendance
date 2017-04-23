import React, { Component, PropTypes } from 'react'
import { Button } from 'react-bootstrap'
import Form from 'react-formal'
import types from 'react-formal-inputs'
import yup from 'yup'
import { SLIP_TYPES, INFORMED, SLIP_TYPE_LOOKUP, TA_IS_INFORMED } from '../constants'
import { LeaveSlipSchema } from './schemas'
import LeaveSlipNote from './LeaveSlipNote'
import SelectedEventsField from './SelectedEventsField'
import TAInformedField from './TAInformedField'
import FormSummary from './FormSummary'
import SlipTypesField from './SlipTypesField'

//gives us advanced form inputs like selectlist - see
//https://github.com/jquense/react-formal-inputs
//http://jquense.github.io/react-widgets/docs/
Form.addInputTypes(types)

const LeaveSlipForm = ({...props}) => {
  let schema = LeaveSlipSchema(props);
  return (
    <div className='dt-leaveslip'>
      <h4 className='dt-leaveslip__title'>Submit Leaveslip</h4>
      <Form
        schema={schema}
        value={props.form}
        onChange={props.changeLeaveSlipForm}
        onSubmit={props.postLeaveSlip}
      >
        <SelectedEventsField />

        <SlipTypesField lastSlips={props.lastSlips} />

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
        <Form.Field type='textarea' name='comment' className='dt-leaveslip__comments'/>

        <TAInformedField taInformed={props.form.ta_informed} tas={props.tas} />

        <FormSummary />

        <LeaveSlipNote />

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
