affectsPerfectAttendance = {};

function updatePerfectAttendance(node) {
	if(updatePerfectAttendance.enabled) {
		var value = node.value;
		var cb = dojo.byId("perfectAttendanceCheckbox");
		if(cb) {
			cb.checked = !affectsPerfectAttendance[value];
		}
	}
}



updatePerfectAttendance.enabled = true;
