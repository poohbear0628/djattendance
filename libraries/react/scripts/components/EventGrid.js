import React from 'react'
import PropTypes from 'prop-types'
import EventColumn from './EventColumn'
import TimesColumn from '../components/TimesColumn'
import { joinValidClasses } from '../constants'

const EventGrid = ({eventsByCol, selectedEvents, onEventClick, onHeaderClick, show}) => {
  return (
    <div className="col-md-12">
      <div className="row">
        <TimesColumn />
        {eventsByCol.map((daysEsr, i) =>
          {
            return (<EventColumn
              key={i}
              {...daysEsr}
              onEventClick={(ev) => onEventClick(ev)}
              onHeaderClick={(evs) => onHeaderClick(evs)}
              selectedEvents={selectedEvents}
            />)
          }
        )}
      </div>
    </div>  
  )
}

EventGrid.propTypes = {
  eventsByCol: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  onEventClick: PropTypes.func.isRequired
}

export default EventGrid
