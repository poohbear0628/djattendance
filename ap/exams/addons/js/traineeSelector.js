function tsInit()
{
	var traineeSelector = dojo.html.createNodesFromText(
'<div id="traineeSelector" class="resizeMe">\n' +
'	<input type="hidden" id="tsInputForID" name="tsInputForID" value="" />\n' +
'	<input type="hidden" id="tsInputForName" name="tsInputForName" value="" />\n' +
'	<input type="hidden" id="tsScheduleInstID" name="tsScheduleInstID" value="" />\n' +
'	<input type="hidden" id="tsSwgID" name="tsSwgID" value="" />\n' +
'	<span id="tsSWGNameSpan" style="position:absolute; top:2px; left:10px"></span>\n' +
'	<a href="javascript:tsHide()" style="position:absolute; top:2px; right:10px">Close Window</a>\n' +
'  	<table>\n' +
'		<tr>\n' +
'			<td>\n' +
'				<div id="tsFilterTableDiv">\n' +
'				</div>\n' +
'			</td>\n' +
'			<td>&nbsp;&nbsp;&nbsp;</td>\n' +
'			<td>\n' +
'				<div id="tsTraineeTableDiv">\n' +
'				</div>\n' +
'			</td>\n' +
'		</tr>\n' +
'	</table>\n' +
'</div>', true)[0];

	dojo.body().appendChild(traineeSelector);
}

function tsShow(_scheduleInstID, _swgID, inputForID, inputForName)
{
	/////////////////////////
	// Save the parameters //
	/////////////////////////

	document.getElementById("tsScheduleInstID").value = _scheduleInstID;
	document.getElementById("tsSwgID").value = _swgID;
	document.getElementById("tsInputForID").value = inputForID;
	document.getElementById("tsInputForName").value = inputForName;

	///////////////////////////////
	// Do AJAX submit using dojo //
	///////////////////////////////

	dojo.io.bind(
	{
		url: fttaUrl("/serviceScheduler/traineeSelector_ajax.php"),
		method: "post",
		content:
		{
		    action:"show",
			scheduleInstID:_scheduleInstID,
			swgID:_swgID
		},
		mimetype: "text/json",
		load:
			function(type, data, xhr)
			{
				document.getElementById("tsSWGNameSpan").innerHTML = data.swgName;
				document.getElementById("tsFilterTableDiv").innerHTML = data.filterTableHTML;
				document.getElementById("tsTraineeTableDiv").innerHTML = data.traineeTableHTML;
				ts_makeSortable(document.getElementById("tsTraineeTable"));
				ts_makeSortable(document.getElementById("tsFilterTable"));

				//////////////////////////////////
				// Display the trainee selector //
				//////////////////////////////////

				var ts = document.getElementById("traineeSelector");
				
				if (document.all) // For IE
				{
					ts.style.top = document.body.scrollTop + 10;
					ts.style.left = document.body.scrollLeft + 10;
				}
				else // For Firefox
				{
					ts.style.top = window.pageYOffset + 10;
					ts.style.left = window.pageXOffset + 10;
				}

				ts.style.display = "block";
			}
	});
}

function tsUpdate()
{
	/////////////////////////
	// Retrieve saved info //
	/////////////////////////

	var _scheduleInstID = document.getElementById("tsScheduleInstID").value;
	var _swgID = document.getElementById("tsSwgID").value;

	///////////////////////////////////
	// Get the show conflict setting //
	///////////////////////////////////

	var _showConflicts;
	var showConflictsCB = document.getElementById("tsShowConflicts");

	if (showConflictsCB)
	    _showConflicts = (showConflictsCB.checked? 1 : 0);

	////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Get the selected filters (formatted as a comma delimited string so that it can be passed to ajax page) //
	////////////////////////////////////////////////////////////////////////////////////////////////////////////

	var firstTime = true;
	var _selectedFilters = "";
	var filterInputs = document.getElementById('tsFilterTable').getElementsByTagName("input");

	for (i = 0; i < filterInputs.length; i++)
	    if (filterInputs[i].checked)
	    {
	        if (firstTime)
	            firstTime = false;
			else
			    _selectedFilters += ',';
			
	        _selectedFilters += filterInputs[i].id.substr(6, filterInputs[i].id.length - 6);
		}

	///////////////////////////////
	// Do AJAX submit using dojo //
	///////////////////////////////

	dojo.io.bind(
	{
		url: fttaUrl("/serviceScheduler/traineeSelector_ajax.php"),
		method: "post",
		content:
		{
		    action:"update",
			scheduleInstID:_scheduleInstID,
			swgID:_swgID,
			showConflicts:_showConflicts,
			selectedFilters:_selectedFilters
		},
		mimetype: "text/json",
		load:
			function(type, data, xhr)
			{
				document.getElementById("tsTraineeTableDiv").innerHTML = data.traineeTableHTML;
				ts_makeSortable(document.getElementById("tsTraineeTable"));
			}
	});
}

function tsHide()
{
	document.getElementById("traineeSelector").style.display = "none";
}

function tsCopyValues(traineeID, traineeName)
{
	var inputForID = document.getElementById("tsInputForID").value;
	var inputForName = document.getElementById("tsInputForName").value;
	document.getElementById(inputForID).value = traineeID;
	document.getElementById(inputForName).value = traineeName;

	tsHide();
}

dojo.addOnLoad(
	function()
	{
		tsInit();
	}
);
