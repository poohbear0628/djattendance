import React from 'react'
import Form from 'react-formal'

const SubmitButton = (props) => {
  return (
  <div>
    {!props.finalized && <Form.Button className='dt-submit btn btn-primary' type='submit'>Submit</Form.Button>}
  </div>
  )
}

export default SubmitButton
