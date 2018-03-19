import React from 'react'
import { Button } from 'react-bootstrap'
import Form from 'react-formal'

const SubmitButton = (props) => {
  return (
  <div>
      {!props.finalized && <Form.Button className='dt-submit' type='submit'>Submit</Form.Button>}
  </div>
  )
}

export default SubmitButton
