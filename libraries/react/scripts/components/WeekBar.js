import React from 'react'
import PropTypes from 'prop-types'
import { format } from 'date-fns'
import Select from 'react-select';

const WeekBar = ({isFirst, firstStart, firstEnd, secondStart, secondEnd, period, currentPeriod,
                    onPrevWeek, onNextWeek, onPrevPeriod, onNextPeriod, traineeView, selectPeriod}) =>
{
  let periodChoices = Array.from(Array(currentPeriod).keys()).map(c => { return {value: c, label: c}})
  let selectedPeriod = {value: period, label: period}
  return (
    <div>
      <div className="weekbar">
        <span className="weekbar__title">
          WEEK {period * 2 + (isFirst ? 0 : 1)} PERIOD
          <Select className="weekbar__period" clearable={false} options={periodChoices} value={selectedPeriod} onChange={selectPeriod}/>
        </span>
      </div>
      <div className="weekbar-sub">
        <div className="btn-toolbar" role="toolbar">
          <div className="btn-group">
            <button className="weekbar-sub__prev btn btn-default" disabled={period == 0} onClick={onPrevPeriod}>&lt;</button>
            <button className="weekbar-sub__date-range btn btn-default" disabled={isFirst} onClick={onPrevWeek}>
              {format(firstStart, 'M/D')} - {format(firstEnd, 'M/D')}
            </button>
            <button className="weekbar-sub__date-range btn btn-default" disabled={!isFirst} onClick={onNextWeek}>
              {format(secondStart, 'M/D')} - {format(secondEnd, 'M/D')}
            </button>
            <button className="weekbar-sub__next btn btn-default" disabled={period == 9} onClick={onNextPeriod}>&gt;</button>
          </div>
        </div>
      </div>
    </div>
  )
}

WeekBar.propTypes = {
  isFirst: PropTypes.bool.isRequired,
  onPrevWeek: PropTypes.func.isRequired,
  onNextWeek: PropTypes.func.isRequired,
  onPrevPeriod: PropTypes.func.isRequired,
  onNextPeriod: PropTypes.func.isRequired
};

export default WeekBar
