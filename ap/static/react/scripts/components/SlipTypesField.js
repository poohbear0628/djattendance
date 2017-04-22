import React from 'react'
import Form from 'react-formal'

import { SLIP_TYPES, SLIP_TYPE_LOOKUP } from '../constants'

let SlipTypesField = (props) => {
  let slipTypes = SLIP_TYPES
  let addLastSlips = (slips) => {
    let slipIds = slips.map((s) => s.type)
    let dates = slips.map((s) => s.events.slice(-1)[0].date)
    slipTypes = SLIP_TYPES.map((s) => {
      let index = slipIds.indexOf(s.id)
      if (index >= 0) {
        return {
          id: s.id,
          name: s.name + ' (last slip: ' + dates[index] + ')'
        }
      }
      return s
    })
  }
  addLastSlips(props.lastSlips)

  return (
    <div>
      <b>Reason</b>
      <Form.Field type='dropdownList' placeholder='Choose a reason' data={slipTypes} name='slipType' valueField='id' textField='name' />
    </div>
  )
}

export default SlipTypesField
