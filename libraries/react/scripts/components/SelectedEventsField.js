import React from 'react'
import Form from 'react-formal'

const SelectedEventsField = (props) => {
  return (
  <div>
    <b>Selected Events</b>
    <Form.Field type='multiSelect' name='selectedEvents' valueField='id' textField='code' className='dt-leaveslip__multi' />
  </div>
  )
}

export default SelectedEventsField
