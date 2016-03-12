import React, { PropTypes } from 'react'
import EventColumn from './EventColumn'

import { joinValidClasses } from '../constants'

const EventGrid = ({events_by_day}) => {
  return (
    <div>
      {events_by_day.map(days_events =>
        <EventColumn
          {...days_events}
        />
      )}
    </div>
  )
}

EventGrid.propTypes = {
  events_by_day: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired
}

export default EventGrid
