import React, { PropTypes } from 'react'
import EventView from './EventView'

const EventColumn = ({events}) => {
  // console.log('days_events:', events)
  // var column = []
  // for (int i = 0; i < events.length; i++) {
  //   column.push(<EventView event={events[i].event} slip={events[i].slip} roll={events[i].roll} key={events[i].event.id} />);
  // }

  return (
    <div className="day event-col col-md-1 col-xs-1 no-padding">
      {events.map(function(event) {
        if (event) {
          return <EventView {...event} />
        }
      })}
    </div>
  )
}

EventColumn.PropTypes = {
  events: PropTypes.arrayOf(PropTypes.shape({
    event: PropTypes.object.isRequired,
    roll: PropTypes.object.isRequired,
    slip: PropTypes.object.isRequired,
  }).isRequired).isRequired
}

export default EventColumn