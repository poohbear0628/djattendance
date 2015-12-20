import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { nextWeek, prevWeek, toggleEvent, setRollStatus } from '../actions'
import trainee from '../testdata/trainee'
import rolls from '../testdata/rolls'
import events from '../testdata/events'
import slips from '../testdata/slips'
import Trainee from '../components/Trainee'
import WeekBar from '../components/WeekBar'
import DaysRow from '../components/DaysRow'

class Attendance extends Component {
  render() {
    const { dispatch, trainee, date, events, rolls, slips, selectedEvents } = this.props
    return (
      <div>
        <div>
        <Trainee trainee={trainee} />
        <WeekBar  
          date={date} 
          onPrevClick={date => dispatch(prevWeek(date))}
          onNextClick={date => dispatch(nextWeek(date))}/>
        <hr />
        <div className="row">
          <DaysRow date={date} />
        </div>
        {/*<div className="row">
          <TimesColumn />
          <EventGrid
          events={events}
          rolls={rolls}
          slips={slips}
          date={date} />
          <div className="col-md-4 action-col">
          <RollView  selectedEvents={selectedEvents} />
          </div>
        </div>*/}
        </div>
        <hr />
      </div>
    )
  }
}

Attendance.propTypes = {
  trainee: PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.number,
    active: PropTypes.bool
  }).isRequired,
  date: PropTypes.object.isRequired,
  events: PropTypes.array.isRequired,
  rolls: PropTypes.array.isRequired,
  slips: PropTypes.array.isRequired,
  selectedEvents: PropTypes.array
}

function select(state) {
  return {
    trainee: state.trainee,
    date: state.date,
    events: state.events,
    rolls: state.rolls,
    slips: state.slips,
    selectedEvents: state.selectedEvents,
  }
}

export default connect(select)(Attendance)
