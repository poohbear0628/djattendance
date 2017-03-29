import React, { Component, PropTypes } from 'react'
import Select from 'react-select'

//TODO: customize select options
// see https://github.com/JedWatson/react-select/blob/master/examples/src/components/CustomComponents.js
export default class TraineeSelect extends Component {
  render() {
    const {value, onBlur, onChange, ...props} = this.props; // onBlur and value was on this.props.fields.myField in MyForm
    return <Select
      value={value || ''}          // because react-select doesn't like the initial value of undefined
      onBlur={() => onBlur(value)} // just pass the current value (updated on change) on blur
      onChange={(newValue) => onChange(newValue)}
      multi={true}
      tabSelectsValue={false}
      {...props}
    />;
  }
}