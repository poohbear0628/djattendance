import dateFns from 'date-fns'

//constants
export const ATTENDANCE_MONITOR_GROUP = 4

export const ATTENDANCE_STATUS = [
  {id: 'P', name: 'Present'},
  {id: 'A', name: 'Absent'},
  {id: 'T', name: 'Tardy'},
  {id: 'U', name: 'Uniform'},
  {id: 'L', name: 'Left Class'},
]

export const ATTENDANCE_STATUS_LOOKUP = {
    'P': 'present',
    'A': 'absent',
    'T': 'tardy',
    'U': 'uniform',
    'L': 'left-class'
}

export const SLIP_STATUS_LOOKUP = {
    'A': 'approved',
    'P': 'pending',
    'F': 'fellowship',
    'D': 'denied',
    'S': 'approved' //by TA sister
}

export const SLIP_TYPES = [
  {id: 'SICK', name: 'Sickness'},
  {id: 'SERV', name: 'Service'},
  {id: 'FWSHP', name: 'Fellowship'},
  {id: 'NIGHT', name: 'Night Out'},
  {id: 'MEAL', name: 'Meal Out'},
  {id: 'INTVW', name: 'Interview'},
  {id: 'GOSP', name: 'Gospel'},
  {id: 'CONF', name: 'Conference'},
  {id: 'WED', name: 'Wedding'},
  {id: 'FUNRL', name: 'Funeral'},
  {id: 'SPECL', name: 'Special'},
  {id: 'OTHER', name: 'Other'},
  {id: 'EMERG', name: 'Family Emergency'},
  {id: 'NOTIF', name: 'Notification Only'},
]

export const INFORMED = [
  {id: 'true', name: 'TA informed:'},
  {id: 'false', name: 'Did not inform training office'},
  {id: 'texted', name: 'Texted attendance number (for sisters during non-front office hours only)'},
]

export const SLIP_TYPE_LOOKUP = {
    'CONF': 'Conference',
    'EMERG': 'Family Emergency',
    'FWSHP': 'Fellowship',
    'FUNRL': 'Funeral',
    'GOSP': 'Gospel',
    'INTVW': 'Grad School/Job Interview',
    'GRAD': 'Graduation',
    'MEAL': 'Meal Out',
    'NIGHT': 'Night Out',
    'OTHER': 'Other',
    'SERV': 'Service',
    'SICK': 'Sickness',
    'SPECL': 'Special',
    'WED': 'Wedding',
    'NOTIF': 'Notification Only'
}

export const LEAVE_SLIP_OTHER_TYPES = [
    "INTVW",
    "GOSP",
    "CONF",
    "WED",
    "FUNRL",
    "SPECL",
    "OTHER",
    "EMERG"
]

export const FA_ICON_LOOKUP = {
    "pending": "refresh",
    "denied": "minus-square",
    "approved": "check-square-o"
}

export function sortEsr(e1,e2) {
    var d1 = Date.parse(e1.event['start']);
    var d2 = Date.parse(e2.event['start']);
    if (d1 < d2) {
    return -1;
    } else if (d1 > d2) {
    return 1;
    } else {
    return 0;
    }
}

export function sortEvents(e1,e2) {
    var d1 = Date.parse(e1['start']);
    var d2 = Date.parse(e2['start']);
    if (d1 < d2) {
    return -1;
    } else if (d1 > d2) {
    return 1;
    } else {
    return 0;
    }
}

export function joinValidClasses(classes) {
  return _.compact(classes).join(' ');
};

export function categorizeEventStatus(wesr) {
  //absenses unexcused
  var status = ''
  if(wesr[i].slip === null) {
    status = 'unexcused'
  } else if(wesr[i].slip["status"] == "D" || wesr[i].slip["status"] == "P" || wesr[i].slip["status"] == "F") {
    status = 'pending'
  } else if(wesr[i].slip && wesr[i].slip["status"] == "A") {
    status = 'approved'
  }

  if(wesr[i].roll && wesr[i].roll["status"] == "A") {
    status += " absent"
  } else if(wesr[i].roll && (wesr[i].roll["status"] == "T" || wesr[i].roll["status"] == "U" || wesr[i].roll["status"] == "L")) {
    status += "tardy"
  }
  return status
}

export function canSubmitRoll(dateDetails) {
  let weekStart = dateDetails.weekStart
  let weekEnd = dateFns.addDays(dateDetails.weekEnd, 1)
  let rollDate = new Date()
  return (rollDate >= weekStart && rollDate <= weekEnd)
}

export function canFinalizeRolls(rolls, dateDetails) {
  let weekStart = dateDetails.weekStart
  let weekEnd = dateDetails.weekEnd
  let rollsThisWeek = rolls.filter(function(roll) {
    let rollDate = new Date(roll.date)
    return rollDate >= weekStart && rollDate <= weekEnd
  })
  let isWeekFinalized = rollsThisWeek.filter(function(roll) {
    return roll.finalized == false
  }).length === 0
  let weekHasRolls = rollsThisWeek.length > 0
  let now = new Date()
  // Sunday midnight is when you can start finalizing
  weekEnd = dateFns.addDays(weekEnd, -1)
  let isPastSundayMidnight = now >= weekEnd
  // Tuesday midnight is when you can no longer finalize
  weekEnd = dateFns.addDays(weekEnd, 2)
  let isBeforeTuesdayMidnight = now <= weekEnd
  let canFinalizeWeek = !isWeekFinalized && isPastSundayMidnight && isBeforeTuesdayMidnight && weekHasRolls
  return canFinalizeWeek
}
