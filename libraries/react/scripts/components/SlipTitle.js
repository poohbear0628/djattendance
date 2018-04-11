import React, { Component } from 'react'
import { Button } from 'react-bootstrap'

const SlipTitle = (props) => {
  let actionText
  if (!props.form.id) {
    actionText = 'Submit'
  } else if (props.form.finalized) {
    actionText = 'View'
  } else {
    actionText = 'Edit'
  }
  return (
    <h4 className='dt-leaveslip__title'>
      {actionText + ' Leave Slip'}&nbsp;
      {props.form.id && <Button onClick={props.resetForm} className="pull-right" bsSize="small">New Leave Slip</Button>}
    </h4>
  )
}

export default SlipTitle
