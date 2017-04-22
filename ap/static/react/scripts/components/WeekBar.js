import React, { PropTypes } from 'react'
import { format } from 'date-fns'

const WeekBar = ({isFirst, firstStart, firstEnd, secondStart, secondEnd, period,
                    onPrevWeek, onNextWeek, onPrevPeriod, onNextPeriod, traineeView}) =>
(
  <div>
    <div className="weekbar">
      <div className="weekbar__title">
        PERIOD {period}
      </div>
      <div className="weekbar__controls btn-toolbar" role="toolbar">
        <div className="btn-group">
          <button className="weekbar__prev btn btn-default" disabled={period == 0} onClick={onPrevPeriod}>&lt;</button>
          <button className="weekbar__date-range btn btn-default" disabled={isFirst} onClick={onPrevWeek}>
            {format(firstStart, 'M/D')} - {format(firstEnd, 'M/D')}
          </button>
          <button className="weekbar__date-range btn btn-default" disabled={!isFirst} onClick={onNextWeek}>
            {format(secondStart, 'M/D')} - {format(secondEnd, 'M/D')}
          </button>
          <button className="weekbar__next btn btn-default" disabled={period == 9} onClick={onNextPeriod}>&gt;</button>
        </div>
      </div>
    </div>
  </div>
)

WeekBar.propTypes = {
  isFirst: PropTypes.bool.isRequired,
  onPrevWeek: PropTypes.func.isRequired,
  onNextWeek: PropTypes.func.isRequired,
  onPrevPeriod: PropTypes.func.isRequired,
  onNextPeriod: PropTypes.func.isRequired
};

export default WeekBar
