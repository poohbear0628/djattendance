import React, { Component, PropTypes } from 'react'

export default class WeekBar extends Component {
  render() {
    console.log("render props", this.props)
    // var startdate = this.props.date.weekday(0).format('M/D/YY');
    // var enddate = this.props.date.weekday(6).format('M/D/YY');
    return (
      <div className="btn-toolbar" role="toolbar">
        <div className="controls btn-group">
          <button className="btn btn-info"><span className="glyphicon glyphicon-calendar"></span></button>
        </div>
        <div className="controls btn-group">
          <button className="btn btn-default clndr-previous-button" onClick={(e) => this.handlePrev(e)}>Prev</button>
          <div className="daterange btn btn-default disabled">
            {this.props.date.weekday(0).format('M/D/YY')} to {this.props.date.weekday(6).format('M/D/YY')}
          </div>
          <button className="btn btn-default clndr-next-button" onClick={(e) => this.handleNext(e)}>Next</button>
        </div>
      </div>
    );
  }

  handlePrev(e) {
    console.log("hello!", e)
    this.props.onPrevClick(this.props.date)
  }

  handleNext(e) {
    this.props.onNextClick(this.props.date)
  }
}

WeekBar.propTypes = {
  onPrevClick: PropTypes.func.isRequired,
  onNextClick: PropTypes.func.isRequired,
  date: PropTypes.object.isRequired,
}