import { connect } from 'react-redux'
import { nextWeek, prevWeek } from '../actions'
import EventGrid from '../components/EventGrid'

const mapStateToProps = (state) => {
  var weekStart = dateFns.format(dateFns.startOfWeek(state.date), 'M/D/YY'),
      weekEnd = dateFns.format(dateFns.endOfWeek(state.date), 'M/D/YY');

  //get just this week's events
  var week_events_slips_rolls = _.filter(state.eventsSlipsRolls, function(esr) {
    return (new Date(weekStart) < new Date(esr.event['start']) && new Date(weekEnd) > new Date(esr.event['end']));
  }, this);

  //sort events by day of the week
  //esr stands events, slips, rolls
  var cols = [];
  for (var i = 0; i < 7; i++) {
    var day_esr = _.filter(week_events_slips_rolls, function(esr) {
      return dateFns.getDay(esr.event['start']) === i;
    });

    var sorted = day_esr.sort(function (e1,e2) {
      var d1 = Date.parse(e1.event['start']);
      var d2 = Date.parse(e2.event['start']);
      if (d1 < d2) {
        return -1;
      } else if (d1 > d2) {
        return 1;
      } else {
        return 0;
      }
    });

    cols.push({events : sorted});
  }

  return {
    events_by_day: cols,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onEventClick: () => {
    }
  }
}

const GridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(EventGrid)

export default GridContainer