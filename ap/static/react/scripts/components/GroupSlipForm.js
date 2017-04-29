import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import Form from 'react-formal'
import types from 'react-formal-inputs'
import yup from 'yup'

import { SLIP_TYPES, INFORMED } from '../constants'
import { GroupSlipSchema } from './schemas'
import LeaveSlipNote from './LeaveSlipNote'
import SelectedEventsField from './SelectedEventsField'
import TAInformedField from './TAInformedField'
import FormSummary from './FormSummary'
import SlipTypesField from './SlipTypesField'

//gives us advanced form inputs like selectlist - see
//https://github.com/jquense/react-formal-inputs
//http://jquense.github.io/react-widgets/docs/
Form.addInputTypes(types)

const GroupSlipForm = ({...props}) => {
  let schema = GroupSlipSchema(props);
  return (
    <div className="dt-leaveslip">
      <h4 className='dt-leaveslip__title'>Submit GroupSlip</h4>
      <Form
        schema={schema}
        value={props.form}
        onChange={props.changeGroupSlipForm}
        onSubmit={props.postGroupSlip}
      >
        <b>Select Trainees</b>
        <Form.Field type='multiSelect' data={props.trainees} name='trainees' valueField='id' textField='name' className='dt-leaveslip__multi' />

        <SelectedEventsField />

        <SlipTypesField lastSlips={[]} />

        <h4 className='dt-leaveslip__title'>Comments</h4>
        <Form.Field type='textarea' name='comment' className='dt-leaveslip__comments'/>

        <TAInformedField taInformed={props.form.ta_informed} tas={props.tas} />

        <FormSummary />

        <LeaveSlipNote />

        <Form.Button className='dt-submit' type='submit'>Submit Group Leaveslip</Form.Button>
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
