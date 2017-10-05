import React, { Component } from 'react'
import { changeTraineeView } from '../actions'
import PropTypes from 'prop-types'
import Select from 'react-select'
import { ATTENDANCE_MONITOR_GROUP } from '../constants'
import yup from 'yup'

//client side validation
let modelSchema = (props) => {
  return yup.object({
    traineeView: yup.object().required("If you see this, something is wrong."),
  });
}

const TraineeSelector = (props) => {
  let schema = modelSchema(props);
  return (
    props.form.trainee.groups.indexOf(ATTENDANCE_MONITOR_GROUP) >= 0 &&
      <div className="dt-roll__trainee-select">
        <b>Trainee</b>
        <Select name="traineeView" clearable={false} options={props.form.trainees} labelKey='name' valueKey='id' value={props.form.traineeView} onChange={props.changeTraineeView} />
      </div>
    )
}

export default TraineeSelector
