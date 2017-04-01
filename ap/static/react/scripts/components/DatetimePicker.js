import React, { Component, PropTypes } from 'react'
import { DateField } from 'react-date-picker'

export default () => {
  return <DateField
    forceValidDate
    defaultValue={new Date()}
    dateFormat="YYYY-MM-DD hh:mm a"  
  />
}

// export default class DatetimePicker extends Component {
//   render() {
//     const {value, onBlur, onChange, ...props} = this.props; // onBlur and value was on this.props.fields.myField in MyForm
//     return <Datetime
//       value={value || ''}          // because react-select doesn't like the initial value of undefined
//       onBlur={() => onBlur(value)} // just pass the current value (updated on change) on blur
//       onChange={(newValue) => onChange(newValue)}
//       {...props}
//     />;
//   }
// }