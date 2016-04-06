 // Javascript for serviceScheduler/workerProfile/editQualificationGroup.php

 function editQualificationGroup(groupId, name) {
   // Get a new value from the user
   var newName = prompt("Change the name "+name+" to ");
   
   // If the user cancels the name change, then do nothing
   if ((newName == null) || (newName == '')) {
     alert("Cannot change to blank name!  You must specify a new name"); 
     return;
   }
   
   // Do the AJAX submit using dojo
   // The URL is where the data will get sent with "content" as the parameters
   // Then the anonymous load function will get called when the server sends it's response back
   dojo.io.bind({
    url: fttaUrl("/serviceScheduler/workerProfile/editQualificationGroups_ajax.php"),
   	method: "post",
   	content: { newname:newName, qgid:groupId },
   	mimetype: "text/json",
   	load: function(type, data, xhr) {
   		// type == 'load'
   		// xhr = XHMLHttpRequest Object
   		var message = data.message; // created in editQualificationGroups_ajax.php
   		var success = data.success; // stores "0" for failure or "1" for success
   		
   		if (success == '0') {
   		  alert("Failed to update group! "+message);
   		
   		// The update succeeded so update the HTML on the screen
   		} else {
   		  // get the DIV html element with the name
   		  var divName = document.getElementById("namediv_qgid_"+groupId);
   		  if (divName == null) {
   		    alert("Could not find HTML element with name namediv_qgid_"+groupId);
   		    return; // abort
   		  }
   		  // This updates the screen, showing the new name
   		  divName.innerHTML = newName;

        // Now we want to update the feedback div on the screen (not entirely necessary, but nice)
   			var feedbackDiv = document.getElementById("feedback_div");
   			if (feedbackDiv != null) {
   			  feedbackDiv.innerHTML = message; // set the content of the div to the message
   			  feedbackDiv.style.display = "block"; // to show the div 
   			  
   			} else {
   			  alert("Could not find feedback_div to display feedback.  Update succeeded! "+message);
   			} // if feedbackDiv

   		} // if success
   	} // function
   }); // dojo.bind
   
 }