//unfinished stub, keeping in case we ever want a composite schedule view for group slips in the future
var genericEvent = {
	'name': null,
	'code': null,
	'start': null,
	'end': null,
	'day': null, //0 is monday
}

var Composite = [];

for (var i = 1; i < 7; i++) {
	var rise = {
		'name': 'Rise',
		'code': 'Rise',
		'start': '6:30',
		'end': '7:30',
		'day': i
	}
	composite.push(rise);

	var brkf = {
		'name': 'Breakfast and Morning Revival',
		'code': 'Brfk & MR',
		'start': '7:30',
		'end': '8:25',
		'day': i
	}
	composite.push(brkf);

	if (i == 6) {
		var LDMM = {
			'name': "Lord's Day Morning Meeting"
			'code': "LD Morning Meeting",
			'start': '8:00',
			'end': '11:30',
			'day': i
		}
		composite.push(LDMM);
	} else {
		var SessI = {
			'name': 'Session I',
			'code': 'Sess I',
			'start': '8:25',
			'end': '10:15',
			'day': i
		}
		composite.push(SessI);

		var SessII = {
			'name': 'Session II',
			'code': 'Sess II',
			'start': '10:15',
			'end': '11:30',
			'day': i
		}
		composite.push(SessII);
	}
}

module.exports = Composite;