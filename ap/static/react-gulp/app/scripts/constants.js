//constants
export const ATTENDANCE_STATUS_LOOKUP = {
    P: 'present',
    A: 'absent',
    T: 'tardy',
    U: 'uniform',
    L: 'left-class'
}

export const SLIP_STATUS_LOOKUP = {
    'A': 'approved',
    'P': 'pending',
    'F': 'fellowship',
    'D': 'denied',
    'S': 'approved'
}

export const ROLL_CODE_LOOKUP = {
    'BF': 'Breakfast',
    'FM': 'FMoC',
    'GE': 'GE',
    'SP': 'Spirit',
    'GW': 'GOW',
}

export function joinValidClasses(classes) {
  return _.compact(classes).join(' ');
};