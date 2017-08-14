import React from 'react'
import Form from 'react-formal'

const SelectedEventsField = (props) => {
  return (
  <div>
    <Form.Field type='multiSelect' name='selectedEvents' valueField='id' textField='code' className='dt-leaveslip__events' />
  </div>
  )
}

export default SelectedEventsField
