//reducers change state (see reducers.js)
//selectors take state and make it usable by components (selectors turn state into props)
//reselect is a library that memoizes selectors so that it is memory efficient to do so
import { createSelector } from 'reselect'
import dateFns from 'date-fns'

//set manipulations used to do array computations quickly & easily from https://www.npmjs.com/package/set-manipulator
import { union, intersection, difference, complement, equals } from 'set-manipulator';

import { sortEsr, sortEvents } from '../constants'

//defining base states
const form = (state) => state.form
const date = (state) => state.date
const toggle = (state) => state.toggle
const selectedEvents = (state) => state.selectedEvents
const show = (state) => state.show
const rolls = (state) => state.rolls
const leaveslips = (state) => state.leaveslips
const groupslips = (state) => state.groupslips
const events = (state) => state.events
const groupevents = (state) => state.groupevents
const trainee = (state) => state.trainee
const trainees = (state) => state.trainees
const isSecondYear = (state) => state.isSecondYear
const tas = (state) => state.tas
const term = (state) => state.term

export const getDateDetails = createSelector(
  [date, term],
  (date, term) => {
    let startDate = dateFns.startOfWeek(date, {weekStartsOn: 1}),
      endDate = dateFns.endOfWeek(date, {weekStartsOn: 1})

    let difference = dateFns.differenceInWeeks(startDate, new Date(term.start));
    let period = Math.floor(difference/2);

    let firstStart = null;
    let firstEnd = null;
    let secondStart = null;
    let secondEnd = null;
    let isFirst = null;
    if (difference % 2 == 1) {
      secondStart = startDate;
      secondEnd = endDate;
      firstStart = dateFns.addDays(startDate, -7);
      firstEnd = dateFns.addDays(endDate, -7);
      isFirst = false;
    } else {
      firstStart = startDate;
      firstEnd = endDate;
      secondStart = dateFns.addDays(startDate, 7);
      secondEnd = dateFns.addDays(endDate, 7);
      isFirst = true;
    }

    return {
      isFirst: isFirst,
      firstStart: firstStart, 
      firstEnd: firstEnd,
      secondStart: secondStart,
      secondEnd: secondEnd,
      period: period
    }
  }
)


export const traineeMultiSelect = createSelector(
  [trainees],
  (trainees) => {
    return trainees.map((trainee) => {
      return {id: trainee.id, name: trainee.name}
    })
  }
)


export const getEventsforPeriod = createSelector(
  [ getDateDetails, events, groupevents, show ],
  (dates, events, groupevents, show) => {
    if (show === 'groupslip') {
      events = groupevents
    }
    let t = events.filter((o) => {
      //deal with timezone hours offset when creating date.
      let start = new Date(o['start'])
      start.setHours(start.getHours() + start.getTimezoneOffset()/60)
      let end = new Date(o['end'])
      end.setHours(end.getHours() + end.getTimezoneOffset()/60)
      return (dates.firstStart < start && dates.secondEnd > end)
    });
    return t;
  }
)

export const getESRforWeek = createSelector(
  [getEventsforPeriod, leaveslips, groupslips, rolls],
  (week_events, leaveslips, groupslips, rolls) => {
    let esr = [];
    week_events.forEach((event) => {
      let a = [];
      a.event = {...event};
      leaveslips.forEach((slip) => {
        //event ids are strings and slip.event.ids are ints but apparently it doesn't matter... because javascript?
        // FOUND OUT 1 == "1" => true but 1 === "1" => false.
        slip.events.some((ev) => {
          if(ev.id == event.id && ev.date == event.start.split("T")[0]) {
            a.event.slip = {...slip}
            return true;
          }
        return false;
        })
      });
      //if groupslip falls into range of event
      groupslips.some((gsl) => {
        if ((event.start <= gsl.start && event.end > gsl.start)
            || (event.start >= gsl.start && event.end <= gsl.end)
            || (event.start < gsl.end && event.end >= gsl.end)) {
          a.event.gslip = {...gsl};
        return true;
        }
        return false;
      })
      rolls.some((roll) => {
        if(roll.event == event.id && roll.date == event.start.split("T")[0] ) {
          a.event.roll = {...roll}
          return true;
        }
        return false;
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
  (esrs) => {
    let evs = []
    esrs.forEach((esr) => {
      if(esr.event.slip || esr.event.gslip || esr.event.roll) {
        evs.push(esr);
      }
    });
    return evs;
  }
)

export const getEventsByCol = createSelector(
  [getESRforWeek, date],
  (events, date) => {
    let weekStart = dateFns.startOfWeek(date, {weekStartsOn: 1})
    let cols = []
    for (let i = 0; i < 7; i++) {
      let dayESR = events.filter((esr) => {
        let day = dateFns.getDay(esr.event['start'])-1
        return (day < 0 ? day+7 : day) === i && dateFns.startOfWeek(esr.event['start'], {weekStartsOn: 1}).getTime() === weekStart.getTime();
      });

      let sorted = dayESR.sort(sortEsr);
      // have to do some funky business because dateFns.getDay returns LD as first but we want LD to be last
      cols.push(
        {
          date: dateFns.addDays(weekStart, i),
          daysEsr: sorted
        }
      )
    }
    return cols;
  }
)

// export const getLeaveSlipsforWeek = ObjforWeekCreator('slip');
export const getLeaveSlipsforPeriod = createSelector(
  [leaveslips, getDateDetails],
  (ls, dates) => {
    let slips = []
    ls.forEach((slip) => {
      slip.events.some((ev) => {
        console.log(dates, ev)
        if(dates.firstStart < new Date(ev['date']) && dates.secondEnd > new Date(ev['date'])) {
          console.log('true slip');
          slips.push(slip)
          return true;
        }
      return false;
      })
    });
    return slips;
  }
)

export const getGroupSlipsforPeriod = createSelector(
  [groupslips, getDateDetails],
  (ls, dates) => {
    let slips = []
    ls.forEach((slip) => {
      //event ids are strings and slip.event.ids are ints but apparently it doesn't matter... because javascript?
      // FOUND OUT 1 == "1" => true but 1 === "1" => false.
      // TODO: Needs to figure out what we will show here.
      if(dates.firstStart < new Date(slip['start']) && dates.secondEnd > new Date(slip['end'])) {
        slips.push(slip)
        return true;
      } else {
        return false;
      }
    });
    return slips;
  }
)

export const getTAs = createSelector(
  [tas], (tas) => {
    let ta_names = [];
    for (let i = 0; i < tas.length; i++) {
      ta_names.push(tas[i].firstname + ' ' + tas[i].lastname);
    }
    return ta_names;
  }
)

export const getTraineeSelect = createSelector(
  [trainees], (trainees) => {
    let traineeSelectOptions = [];
    for (let i = 0; i < trainees.length; i++) {
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