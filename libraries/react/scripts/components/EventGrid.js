import React from 'react'
import PropTypes from 'prop-types'
import EventColumn from './EventColumn'
import TimesColumn from '../components/TimesColumn'
import { joinValidClasses } from '../constants'

const EventGrid = ({eventsByCol, selectedEvents, show, onEventClick, onGroupEventClick, onHeaderClick}) => {
  var eventClickFunction = show == 'groupslip' ? onGroupEventClick : onEventClick
  var headerClickFunction = show == 'groupslip' ? (evs) => {return} : onHeaderClick
  return (
    <div className="col-md-12">
      <div className="row">
        <TimesColumn />
        {eventsByCol.map((daysEsr, i) =>
          {
            return (<EventColumn
              key={i}
              {...daysEsr}
              onEventClick={(ev) => eventClickFunction(ev)}
              onHeaderClick={(evs) => headerClickFunction(evs)}
              selectedEvents={selectedEvents}
              show={show}
            />)
          }
        )}
      </div>
    </div>  
  )
}

EventGrid.propTypes = {
  eventsByCol: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  onEventClick: PropTypes.func.isRequired,
  onGroupEventClick: PropTypes.func.isRequired,
}

export default EventGrid
