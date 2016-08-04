import React, { PropTypes } from 'react'

const WeekBar = ({isFirst, firstStart, firstEnd, secondStart, secondEnd, period,
                    onPrevWeek, onNextWeek, onPrevPeriod, onNextPeriod}) =>
(
  <div className="weekbar">
    <div className="weekbar__controls btn-toolbar" role="toolbar">
      <div className="btn-group">
        <button className="weekbar__prev btn btn-default" disabled={period == 0} onClick={onPrevPeriod}>&lt;</button>
        <button className="weekbar__date-range btn btn-default" disabled={isFirst} onClick={onPrevWeek}>
          {firstStart} - {firstEnd}
        </button>
        <button className="weekbar__date-range btn btn-default" disabled={!isFirst} onClick={onNextWeek}>
          {secondStart} - {secondEnd}
        </button>
        <button className="weekbar__next btn btn-default" disabled={period == 9} onClick={onNextPeriod}>&gt;</button>
      </div>
    </div>
    <div className="weekbar__title">
      PERIOD {period}
    </div>
  </div>
)

WeekBar.propTypes = {
  isFirst: PropTypes.bool.isRequired,
  firstStart: PropTypes.string.isRequired,
  firstEnd: PropTypes.string.isRequired,
  secondStart: PropTypes.string.isRequired,
  secondEnd: PropTypes.string.isRequired,
  onPrevWeek: PropTypes.func.isRequired,
  onNextWeek: PropTypes.func.isRequired,
  onPrevPeriod: PropTypes.func.isRequired,
  onNextPeriod: PropTypes.func.isRequired
};

export default WeekBar
