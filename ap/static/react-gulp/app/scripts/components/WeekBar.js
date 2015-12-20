import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'

class WeekBar extends Component {
  render() {
    console.log(dateFns)
    var startdate = dateFns.format(dateFns.startOfWeek(this.props.date), 'M/D/YY');
    var enddate = dateFns.format(dateFns.endOfWeek(this.props.date), 'M/D/YY');
    return (
      <div className="btn-toolbar" role="toolbar">
        <div className="controls btn-group">
          <button className="btn btn-info"><span className="glyphicon glyphicon-calendar"></span></button>
        </div>
        <div className="controls btn-group">
          <button className="btn btn-default clndr-previous-button" onClick={(e) => this.handlePrev(e)}>Prev</button>
          <div className="daterange btn btn-default disabled">
            {startdate} to {enddate}
          </div>
          <button className="btn btn-default clndr-next-button" onClick={(e) => this.handleNext(e)}>Next</button>
        </div>
      </div>
    );
  }

  handlePrev(e) {
    this.props.onPrevClick(this.props.date);
  }

  handleNext(e) {
    this.props.onNextClick(this.props.date);
  }
}

WeekBar.propTypes = {
  onPrevClick: PropTypes.func.isRequired,
  onNextClick: PropTypes.func.isRequired,
  date: PropTypes.object.isRequired,
};

// Which part of the Redux global state does our component want to receive as props?
function mapStateToProps(state) {
  return {
    date: state.date
  };
}

// Which action creators does it want to receive by props?
function mapDispatchToProps(dispatch) {
  return {
    handlePrev: (date) => dispatch(prevWeek(date)),
    handleNext: (date) => dispatch(nextWeek(date)),
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(WeekBar);