//unfinished stub, keeping in case we ever want a composite schedule view for group slips in the future
var genericEvent = {
	'name': null,
	'code': null,
	'start_datetime': null,
	'end_datetime': null,
	'day': null, //0 is monday
}

var Composite = [];

for (var i = 1; i < 7; i++) {
	var rise = {
		'name': 'Rise',
		'code': 'Rise',
		'start_datetime': '6:30',
		'end_datetime': '7:30',
		'day': i
	}
	composite.push(rise);

	var brkf = {
		'name': 'Breakfast and Morning Revival',
		'code': 'Brfk & MR',
		'start_datetime': '7:30',
		'end_datetime': '8:25',
		'day': i
	}
	composite.push(brkf);

	if (i == 6) {
		var LDMM = {
			'name': "Lord's Day Morning Meeting"
			'code': "LD Morning Meeting",
			'start_datetime': '8:00',
			'end_datetime': '11:30',
			'day': i
		}
		composite.push(LDMM);
	} else {
		var SessI = {
			'name': 'Session I',
			'code': 'Sess I',
			'start_datetime': '8:25',
			'end_datetime': '10:15',
			'day': i
		}
		composite.push(SessI);

		var SessII = {
			'name': 'Session II',
			'code': 'Sess II',
			'start_datetime': '10:15',
			'end_datetime': '11:30',
			'day': i
		}
		composite.push(SessII);
	}
}

module.exports = Composite;
