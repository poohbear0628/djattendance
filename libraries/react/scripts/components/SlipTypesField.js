import React from 'react'
import Form from 'react-formal'

let SlipTypesField = (props) => {
  let slipTypes = props.slipTypes
  let addLastSlips = (slips) => {
    let slipIds = slips.map((s) => s.type)
    let dates = slips.map((s) => s.events.slice(-1)[0].date)
    slipTypes = props.slipTypes.map((s) => {
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
      <Form.Field type='selectlist' data={slipTypes} name='slipType' valueField='id' textField='name' />
    </div>
  )
}

export default SlipTypesField
