//constants
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
  let status = {};
  if (!wesr.slip && !wesr.gslip) {
    status['slip'] = 'unexcused'
  } else {
    if ((wesr.slip && (wesr.slip.status === "D" || wesr.slip.status === "P" || wesr.slip.status === "F")) 
        || (wesr.gslip && (wesr.gslip.status === "D" || wesr.gslip.status === "P" || wesr.gslip.status === "F"))) {
      status['slip'] = 'pending'
    }
    if ((wesr.slip && wesr.slip.status === "D" ) || (wesr.gslip && wesr.gslip.status === "D")) {
        status['slip'] = 'denied'
    } 
    if ((wesr.slip && wesr.slip.status === "A") || (wesr.gslip && wesr.gslip.status === "A")) {
      status['slip'] = 'approved'
    }
  }

  if(wesr.roll && wesr.roll.status === "A") {
    status['roll'] = 'absent'
  } else if(wesr.roll && (wesr.roll.status === "T" || wesr.roll.status === "U" || wesr.roll.status === "L")) {
    status['roll'] = 'tardy'
  }
  return status;
}