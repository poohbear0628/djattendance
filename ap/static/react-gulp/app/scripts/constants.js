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
	'S': 'approved'
}

export const EVENT_CODE_LOOKUP = {
	//Meals
	'BF': 'BF',
	'LU': 'Lun',
	'DN': 'Din',

	//Classes
	'MV': 'Mon Rev',
	'FM': 'FMoC',
	'GW': 'GOW',
	'MM': 'Min Meet',
	'GE': 'GE',
	'SP': 'Spirit',
	'VC': 'Video',
	'PS': 'PSRP',
	'TG': 'Triune God',
	'BCI': 'BOC I',
	'ECI': 'ECAL I',
	'CY': 'CYPC',
	'GKI': 'Gk I',

	//House
	'RI': 'Rise',
	'PR': 'Prayer',
	'LI': 'Lights',
	'CU': 'Curfew',

	//Team and Study
	'ST': 'Study',
	'ES': 'End',
	'TS': 'Team Study',
	'TF': 'TF',
	'TFWK': 'TF & WK',
	'WK': 'Work',

	//Church Meetings
	'PM': 'PM',
	'SG': 'SG',
	'LP': 'LT & PM'
}

export const TERM_START = new Date('2016-02-22')

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