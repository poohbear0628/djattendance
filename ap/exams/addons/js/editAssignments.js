function setAssignmentValuesForEditing(swgID, traineeID)
{
	////////////////////////////////////////
	// Update the trainee ID hidden input //
	////////////////////////////////////////

	var traineeIdInput = document.getElementById("traineeID");

	if (traineeID == -1)
		traineeIdInput.value = document.getElementById("traineeID" + swgID).value;
	else
		traineeIdInput.value = traineeID;

	/////////////////////////////////////////////////////
	// Update the service worker group ID hidden input //
	/////////////////////////////////////////////////////

	var swgIdInput = document.getElementById("swgID");

	if (swgID == -1)
		swgIdInput.value = document.getElementById("swgID" + traineeID).value;
	else
		swgIdInput.value = swgID;
}

function setServiceForEditing(serviceID)
{
	
	/////////////////////////////////////////////////////
	// Update the service worker group ID hidden input //
	/////////////////////////////////////////////////////

	var serviceIDInput = document.getElementById("serviceID");
	serviceIDInput.value = serviceID;
	
}

function enterEditModeForTrainee(traineeID)
{
	var traineeIdInput = document.getElementById("traineeID");
	traineeIdInput.value = traineeID;

	/////////////////////////
	// Enter the edit mode //
	/////////////////////////

	var editModeInput = document.getElementById("editMode");
	editModeInput.value = "edit";

	editModeInput.form.submit();
}

function enterEditModeForService(serviceID)
{
	var serviceIdInput = document.getElementById("serviceID");
	serviceIdInput.value = serviceID;

	/////////////////////////
	// Enter the edit mode //
	/////////////////////////

	var editModeInput = document.getElementById("editMode");
	editModeInput.value = "edit";

	editModeInput.form.submit();
}

function exitEditMode()
{
	var editModeInput = document.getElementById("editMode");
	editModeInput.value = "";
	editModeInput.form.submit();
}
