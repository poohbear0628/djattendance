import { connect } from 'react-redux'
import { toggleEvent, toggleDaysEvents } from '../actions'
import EventGrid from '../components/EventGrid'
import { sortEsr } from '../constants'
import { getEventsByCol } from '../selectors/selectors'

/*
The data structure guide
GridContainer passes an array called cols to EventGrid
GridContainer -----cols[]-----> EventGrid

EventGrid uses .map to pass each object in cols[] to an EventColumn component
EventGrid -----dayEsr-----> EventColumn

dayEsr has a date object and a sorted array of esr's corresponding to the column meaning a particular day
The date object is used for the column header, .map is called on the sorted array to pass on esr objects to EventView

EventColumn -----esr-----> EventView
*/

const mapStateToProps = (state) => {
  return {
    show: state.show,
    eventsByDay: getEventsByCol(state),
    selectedEvents: state.selectedEvents,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onEventClick: (ev) => {
      dispatch(toggleEvent(ev))
    },
    onHeaderClick: (evs) => {
      dispatch(toggleDaysEvents(evs))
    }
  }
}

const GridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(EventGrid)

<<<<<<< HEAD
export default GridContainer
=======
export default GridContainer
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
