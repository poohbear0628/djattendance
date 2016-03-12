import React, { PropTypes } from 'react'

const WeekBar = ({startdate, enddate, onPrevWeek, onNextWeek}) => {
  

  return (
    <div className="btn-toolbar week-bar" role="toolbar">
      <div className="controls btn-group">
        <button className="btn btn-default clndr-previous-button no-margin" onClick={onPrevWeek}>Prev</button>
        <div className="daterange btn btn-default">
          {startdate} - {enddate}
        </div>
        <button className="btn btn-default clndr-next-button" onClick={onNextWeek}>Next</button>
      </div>
    </div>
  )
}

WeekBar.propTypes = {
  onPrevClick: PropTypes.func.isRequired,
  onNextClick: PropTypes.func.isRequired,
  date: PropTypes.object.isRequired
};

export default WeekBar
