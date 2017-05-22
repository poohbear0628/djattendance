import React from 'react'
import PropTypes from 'prop-types'
import { format } from 'date-fns'
import Select from 'react-select';

import SlipStatusIcon from './SlipStatusIcon'

const WeekBar = ({isFirst, firstStart, firstEnd, secondStart, secondEnd, period, currentPeriod, showLegend,
                    onPrevWeek, onNextWeek, traineeView, selectPeriod, toggleLegend}) =>
{
  let periodChoices = Array.from(Array(currentPeriod).keys()).map(c => { return {value: c, label: c}})
  let selectedPeriod = {value: period, label: period}
  return (
    <div>
      <div className="weekbar col-xs-offset-1">
        <span className="weekbar__title">
          WEEK {period * 2 + (isFirst ? 0 : 1)} PERIOD
          <Select className="weekbar__period" clearable={false} options={periodChoices} value={selectedPeriod} onChange={selectPeriod}/>
        </span>
        <span className="weekbar__legend-button pull-right" onClick={toggleLegend}>LEGEND</span>
        {
        showLegend && <span className="weekbar__legend">
          <div className="legend">
            <div className="tardy legend__tardy">Tardy</div>
            <div className="absent legend__absent">Absent</div>
            <div className="excused legend__excused">Excused</div>
            <div>Pending&nbsp;<SlipStatusIcon status='P' /></div>
            <div>Approved&nbsp;<SlipStatusIcon status='A' /></div>
            <div>Denied&nbsp;<SlipStatusIcon status='D' /></div>
            <div>Fellowship&nbsp;<SlipStatusIcon status='F' /></div>
          </div>
        </span>
        }

      </div>
      <div className="weekbar-sub col-xs-offset-1">
        <div className="btn-toolbar" role="toolbar">
          <div className="btn-group">
            <button className="weekbar-sub__date-range btn btn-default" disabled={isFirst} onClick={onPrevWeek}>
              {format(firstStart, 'M/D')} - {format(firstEnd, 'M/D')}
            </button>
            <button className="weekbar-sub__date-range btn btn-default" disabled={!isFirst} onClick={onNextWeek}>
              {format(secondStart, 'M/D')} - {format(secondEnd, 'M/D')}
            </button>
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
};

export default WeekBar
