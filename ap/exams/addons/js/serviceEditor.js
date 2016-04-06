function addServiceTime(btn, timeTable)
{
	var tbl = dojo.byId(timeTable);

	if (!tbl)
		return;

	var throbber = new Throbber(null, null, true);
	throbber.lockButton(btn);
	throbber.insertAfter(btn);

	dojo.io.bind(
		{
			url: "timeScheduleRow.php",
			type: "text/html",
			load:
			function(type, data, evt)
			{
				throbber.done();
				var node = dojo.html.createNodesFromText(data, true)[0];
				tbl.tBodies[0].appendChild(node);
				btn.scrollIntoView(false);
			}
		}
	);
}

function addWorkerGroup(btn)
{
	var throbber = new Throbber(null, null, true);
	throbber.lockButton(btn);
	throbber.insertAfter(btn);

	dojo.io.bind(
		{
			url: "workerGroup.php",
			type: "text/html",
			load:
			function(type, data, evt)
			{
				throbber.done();
				var node = dojo.html.createNodesFromText(data, true)[0];
				dojo.html.insertAfter(node, btn);
				btn.scrollIntoView(true);
			}
		}
	);
}

function deleteServiceTime(btn)
{
	var tr = dojo.html.getParentByType(btn, "tr");
	dojo.html.removeNode(tr);
}

function deleteWorkerGroup(btn)
{
	var div = dojo.html.getParentByType(btn, "div");
	dojo.html.removeNode(div);
}

function hideWorkerGroup(btn, id)
{
	var div = dojo.html.getParentByType(btn, "div");

	// hide it
	if(div)
		div.style.display = "none";

	///////////////////////
	// Mark for deletion //
	///////////////////////

	var elms = div.getElementsByTagName("input");
	var deleteIndicatorName = "swgDeletedStatus" + id;

	for (var i = 0; i < elms.length; i++)
	{
		if (elms[i].name == deleteIndicatorName)
		{
			elms[i].value = 1;
			break;
		}
	}
}
