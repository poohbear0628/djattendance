import React, { PropTypes } from 'react'
import EventColumn from './EventColumn'
import TimesColumn from '../components/TimesColumn'
import { joinValidClasses } from '../constants'

const EventGrid = ({groupEvents, eventsByDay, selectedEvents, onEventClick, onHeaderClick, show}) => {
  var k = 0;
  //if show is groupslips, then render groupEvents instead of eventsByDay.
  console.log(show)
  if (show=='groupslip') {
    return (
      <div className="cal-daywrap">
        <TimesColumn />
        {groupEvents.map(daysEsr =>
          <EventColumn
            key={k++}
            {...daysEsr}
            onEventClick={(ev) => onEventClick(ev)}
            onHeaderClick={(evs) => onHeaderClick(evs)}
            selectedEvents={selectedEvents}
          />
        )}
      </div>
    )
  } else {
    return (
      <div className="cal-daywrap">
        <TimesColumn />
        {eventsByDay.map(daysEsr =>
          <EventColumn
            key={k++}
            {...daysEsr}
            onEventClick={(ev) => onEventClick(ev)}
            onHeaderClick={(evs) => onHeaderClick(evs)}
            selectedEvents={selectedEvents}
          />
        )}
      </div>
    )
  }
}

EventGrid.propTypes = {
  eventsByDay: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  onEventClick: PropTypes.func.isRequired
}

export default EventGrid
