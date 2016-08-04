//reducers change state (see reducers.js)
//selectors take state and make it usable by components (selectors turn state into props)
//reselect is a library that memoizes selectors so that it is memory efficient to do so
import { createSelector } from 'reselect'
import dateFns from 'date-fns'

//set manipulations used to do array computations quickly & easily from https://www.npmjs.com/package/set-manipulator
import { union, intersection, difference, complement, equals } from 'set-manipulator';

import { sortEsr } from '../constants'

//defining base states
const groupslipform = (state) => state.form.groupSlipForm
const rollslipform = (state) => state.form.rollSlipForm
const date = (state) => state.date
const toggle = (state) => state.toggle

const rolls = (state) => state.rolls
const leaveslips = (state) => state.leaveslips
const groupslips = (state) => state.groupslips

const events = (state) => state.events
const trainee = (state) => state.trainee
const trainees = (state) => state.trainees
const isSecondYear = (state) => state.isSecondYear
const tas = (state) => state.tas
const term = (state) => state.term

export const getDateDetails = createSelector(
  [date],
  (date) => {
    //get week start, week end, period start, period end from date
  }
)

export const getEventsforWeek = createSelector(
  [ date, events ],
  (date, events) => {
    let start = dateFns.startOfWeek(date, {weekStartsOn: 1});
    let end   = dateFns.addDays(dateFns.endOfWeek(date, {weekStartsOn: 1}), 1);
    return events.filter((o) => {
      return (start < new Date(o['start']) && end > new Date(o['end']))
    });
  }
)

export const getESRforWeek = createSelector(
  [getEventsforWeek, leaveslips, groupslips, rolls],
  (week_events, leaveslips, groupslips, rolls) => {
    let esr = [];
    week_events.forEach((event) => {
      let a = {event: event};
      leaveslips.forEach((slip) => {
        //event ids are strings and slip.event.ids are ints but apparently it doesn't matter... because javascript?
        // FOUND OUT 1 == "1" => true but 1 === "1" => false.
        if(intersection(slip.events, [event], (ev) => ev.id).length > 0) {
          a.slip = slip;
        }
      }, null);
      //if groupslip falls into range of event
      groupslips.forEach((gsl) => {
        if ((event.start <= gsl.start && event.end > gsl.start)
            || (event.start >= gsl.start && event.end <= gsl.end)
            || (event.start < gsl.end && event.end >= gsl.end)) {
          a.gslip = gsl;
        }
      })
      rolls.forEach((roll) => {
        if(roll.event == event.id) {
          a.roll = roll
        }
      })
      esr.push(a);
    })
    return esr;
  }
)

//get events with roll/ls data, sorted by absenses, tardies, pending & excused
// use constants.js -> categorizeEventStatus to describe the event
export const getEventsByRollStatus = createSelector(
  [getESRforWeek],
  (events) => {
    let evs = []
    events.forEach((ev) => {
      if(ev.slip || ev.gslip || ev.roll) {
        evs.push(ev);
      }
    });
    return evs;
  }
)
export const getEventsByCol = createSelector(
  [getESRforWeek, date],
  (events, date) => {
    var weekStart = dateFns.startOfWeek(date, {weekStartsOn: 1})
    var cols = []

    for (var i = 0; i < 7; i++) {
      var dayESR = events.filter((esr) => {
        return dateFns.getDay(esr.event['start']) === i;
      });

      var sorted = dayESR.sort(sortEsr);
      // have to do some funky business because dateFns.getDay returns LD as first but we want LD to be last
      cols.push(
        {
          date: dateFns.addDays(weekStart, i == 0 ? 6 : i-1), 
          daysEsr: sorted
        }
      )
    }
    //move Lord's Day events to the end of the week
    var ld = cols.splice(0, 1);
    cols.push(ld[0]);

    return cols;
  }
)

//ESR contains all 
const ObjforWeekCreator = (obj) => {
  return createSelector(
    [getESRforWeek],
    (events) => {
      let objs = []
      events.forEach((ev) => {
        if(ev[obj]) {
          objs.push(ev[obj]);
        }
      })
      return objs;
    }
  )
}

// export const getLeaveSlipsforWeek = ObjforWeekCreator('slip');
export const getGroupSlipsforWeek = ObjforWeekCreator('gslip');

export const getLeaveSlipsforWeek = createSelector(
  [getESRforWeek],
  (events) => {
    let slips = []
    events.forEach((ev) => {
      if(ev.slip) {
        slips.push(ev.slip);
      }
    })
    return slips;
  }
)

export const getTAs = createSelector(
  [tas], (tas) => {
    var ta_names = [];
    for (var i = 0; i < tas.length; i++) {
      ta_names.push(tas[i].firstname + ' ' + tas[i].lastname);
    }
    return ta_names;
  }
)

export const getTraineeSelect = createSelector(
  [trainees], (trainees) => {
    var traineeSelectOptions = [];
    for (var i = 0; i < trainees.length; i++) {
      traineeSelectOptions.push({'value': trainees[i].id, 'label': trainees[i].name});
    }
    return traineeSelectOptions;
  }
)

//don't show roll if second year
export const getToggle = createSelector(
  [isSecondYear, toggle], (isSecondYear, toggle) => {
    //never show roll for second year
    if(isSecondYear) {
      return Object.assign({}, toggle, {
        roll: false
      })
    }
    //otherwise let everything through
    return toggle;
  }
)