import React, { PropTypes } from 'react'

const WeekBar = ({isFirst, firstStart, firstEnd, secondStart, secondEnd, 
                    onPrevWeek, onNextWeek, onPrevPeriod, onNextPeriod}) =>
(
  <div className="btn-toolbar week-bar" role="toolbar">
    <div className="controls btn-group">
      <button className="btn btn-default clndr-previous-button no-margin" onClick={onPrevPeriod}>&lt;</button>
      <button className="daterange btn btn-default no-margin" disabled={isFirst} onClick={onPrevWeek}>
        {firstStart} - {firstEnd}
      </button>
      <button className="daterange btn btn-default no-margin" disabled={!isFirst} onClick={onNextWeek}>
        {secondStart} - {secondEnd}
      </button>
      <button className="btn btn-default clndr-next-button" onClick={onNextPeriod}>&gt;</button>
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
