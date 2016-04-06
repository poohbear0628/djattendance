function expandCollapse(idSuffix)
{
	///////////////////////////////////////////
	// Get the anchor and child div elements //
	///////////////////////////////////////////

	var anchorNode = document.getElementById("anchor" + idSuffix);
	var childDiv = document.getElementById("childDiv" + idSuffix);

	/////////////////////////////////////////////////
	// Toggle the display of the child div element //
	/////////////////////////////////////////////////

	if (childDiv.style.display == "none")
	{
		anchorNode.innerHTML = "&ndash;";
		childDiv.style.display = "block";
	}
	else
	{
		anchorNode.innerHTML = "+";
		childDiv.style.display = "none";
	}
}

/***********************************************************************************************************************
Navigating Functions
***********************************************************************************************************************/

function getCB(div)
{
	var table = dojo.html.firstElement(div, "table");
	if(table) {
		var cb = dojo.html.firstElement(table.rows[0].cells[0], "img");
		return cb;
	}
	return null;
}

function getInput(div, inputNum)
{
	var node = div.firstChild;

	while (node && node.nodeName != "TABLE")
		node = node.nextSibling;

	node = node.rows[0].cells[inputNum].firstChild;

	while (node && node.nodeName != "INPUT")
		node = node.nextSibling;

	return node;
}

function topDiv()
{
	return document.getElementById("topDiv");
}

function firstChildDiv(div)
{
	div = div.firstChild;

	while (div && div.nodeName != "DIV")
		div = div.nextSibling;

	div = div.firstChild;

	while (div && div.nodeName != "DIV")
		div = div.nextSibling;

	return div;
}

function nextSiblingDiv(div)
{
	div = div.nextSibling;

	while (div && div.nodeName != "DIV")
		div = div.nextSibling;

	return div;
}

function getParentDiv(div)
{
	return div.parentNode.parentNode;
}

/***********************************************************************************************************************
Checkbox Functions
***********************************************************************************************************************/

var cbStateIndex = "";

function saveServiceCBState(cb, state)
{
	// Save the state in a hidden field if the checkbox is for a service
	if (cb.id != "")
	{
		var serviceID = cb.id.substr(9);
		document.getElementById("cbState" + serviceID).value = state;
	}
}

function toggleCheckbox(cb)
{
	///////////////////////////////
	// Toggle the checkbox state //
	///////////////////////////////

	if (cb.src.substr(cbStateIndex, 1) == "3")
		cbState = "1";
	else
		cbState = "3";

	cb.src = cb.src.substr(0, cbStateIndex) + cbState + ".bmp";
	saveServiceCBState(cb, cbState);
}

function updateChildCheckboxes(cb, id) {
	var box = dojo.byId(id);
	if(box) {
		var divs = box.getElementsByTagName("div");
		for(var i = 0; i < divs.length; i++) {
			var div = divs[i];
			var childCB = getCB(div);
			if(childCB) {
				childCB.src = cb.src;
				saveServiceCBState(childCB, cb.src.substr(cbStateIndex, 1));
			}
		}
	}
}

function updateParentCheckbox(cb)
{
	/////////////////////////////////////////
	// Get the div that the checkbox is in //
	/////////////////////////////////////////

	var div = cb.parentNode;

	while (div && div.nodeName != "DIV")
		div = div.parentNode;

	//////////////////////////////////////////
	// Loop through the sibling check boxes //
	//////////////////////////////////////////

	var parentDiv = getParentDiv(div);
	var someChecked = false;
	var someUnchecked = false;

	for (siblingDiv = firstChildDiv(parentDiv); siblingDiv; siblingDiv = nextSiblingDiv(siblingDiv))
	{
		var siblingCB = getCB(siblingDiv);

		////////////////////////
		// Collect statistics //
		////////////////////////

		if (siblingCB.src.substr(cbStateIndex, 1) == "3")
			someChecked = true;
		else if (siblingCB.src.substr(cbStateIndex, 1) == "1")
			someUnchecked = true;
		else
		{
			someChecked = true;
			someUnchecked = true;
		}
	}

	////////////////////////
	// Indicate selection //
	////////////////////////

	var parentCB = getCB(parentDiv);

	if (someChecked && someUnchecked)
		parentCB.src = parentCB.src.substr(0, cbStateIndex) + "2.bmp";
	else if (someChecked)
		parentCB.src = parentCB.src.substr(0, cbStateIndex) + "3.bmp";
	else
		parentCB.src = parentCB.src.substr(0, cbStateIndex) + "1.bmp";
}

function updateAllParentCheckboxes()
{
	////////////////////////////////////
	// Loop through the category divs //
	////////////////////////////////////

	for (categoryDiv = firstChildDiv(topDiv()); categoryDiv; categoryDiv = nextSiblingDiv(categoryDiv))
	{
		serviceDiv = firstChildDiv(categoryDiv);

		////////////////////////////////////////
		// Set the global stateIndex variable //
		////////////////////////////////////////

		if (cbStateIndex == "")
			cbStateIndex = getCB(categoryDiv).src.lastIndexOf(".bmp") - 1;

		// If there are any services for the category, update its parent checkboxes
		if (serviceDiv)
			updateParentCheckbox(getCB(serviceDiv));
	}
}

/***********************************************************************************************************************
Input Functions
***********************************************************************************************************************/

function updateChildInputs(input, inputNum)
{
	//////////////////////////////////////
	// Get the div that the input is in //
	//////////////////////////////////////

	var div = input.parentNode;

	while (div && div.nodeName != "DIV")
		div = div.parentNode;

	///////////////////////////////////
	// Loop through the child inputs //
	///////////////////////////////////

	for (var childDiv = firstChildDiv(div); childDiv; childDiv = nextSiblingDiv(childDiv))
	{
		//////////////////////////////////////////////
		// Update the selection to match the parent //
		//////////////////////////////////////////////

		var childInput = getInput(childDiv, inputNum);
		childInput.value = input.value;
	}
}

function updateParentInput(input, inputNum)
{
	//////////////////////////////////////
	// Get the div that the input is in //
	//////////////////////////////////////

	var div = input.parentNode;

	while (div && div.nodeName != "DIV")
		div = div.parentNode;

	/////////////////////////////////////
	// Loop through the sibling inputs //
	/////////////////////////////////////

	var parentDiv = getParentDiv(div);
	var firstTime = true;
	var mixedValues = false;
	var firstValue;

	for (siblingDiv = firstChildDiv(parentDiv); siblingDiv; siblingDiv = nextSiblingDiv(siblingDiv))
	{
		var siblingInput = getInput(siblingDiv, inputNum);

		////////////////////////
		// Collect statistics //
		////////////////////////

		if (firstTime)
		{
			firstTime = false;
			firstValue = siblingInput.value;
		}
		else if (siblingInput.value != firstValue)
		{
			mixedValues = true;
			break;
		}
	}

	////////////////////////
	// Indicate selection //
	////////////////////////

	var parentInput = getInput(parentDiv, inputNum);

	if (mixedValues)
		parentInput.value = "*";
	else
		parentInput.value = firstValue;
}

function updateAllParentInputs()
{
	////////////////////////////////////
	// Loop through the category divs //
	////////////////////////////////////

	for (categoryDiv = firstChildDiv(topDiv()); categoryDiv; categoryDiv = nextSiblingDiv(categoryDiv))
	{
		serviceDiv = firstChildDiv(categoryDiv);

		// If there are any services for the category, update its parent inputs
		if (serviceDiv)
		{
			updateParentInput(getInput(serviceDiv, 1), 1);
			updateParentInput(getInput(serviceDiv, 2), 2);
			updateParentInput(getInput(serviceDiv, 3), 3);
		}
	}
}
