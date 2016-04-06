var xmlHttp

function changeValue(str, id)
{ 
xmlHttp=GetXmlHttpObject()
if (xmlHttp==null)
 {
 alert ("Browser does not support HTTP Request")
 return
 }
if (id == "driverID")
{
if (str == '')
{
document.getElementById("driverName").value = ''
document.getElementById("driverPhone").value = ''
document.getElementById("driverDeleteID").value = ''
}
else
{
var url="travelArrangement_ajax.php"
url=url+"?id="+str
url=url+"&sid="+Math.random()
xmlHttp.onreadystatechange=stateChanged
xmlHttp.open("GET",url,true)
xmlHttp.send(null)
}
}
else if (id == "vehicleID")
{
  if (str == '')
  {
     document.getElementById("vehicleName").value = ''
     document.getElementById("vehicleNumPassenger").value = ''
     document.getElementById("vehicleDeleteID").value = ''
  }
  else
  {
    var url="travelArrangement_ajax.php"
    url=url+"?vid="+str
    url=url+"&sid="+Math.random()
    xmlHttp.onreadystatechange=stateChanged2
    xmlHttp.open("GET",url,true)
    xmlHttp.send(null)
  }
}
else if (id == "runID")
{
if (str == '')
  {
    document.getElementById("runTime_hour").selectedIndex = 0
    document.getElementById("runTime_minute").selectedIndex = 0
    document.getElementById("runTime_ampm").selectedIndex = 0
    document.getElementById("runName").value = ''
    document.getElementById("runStartLoc").value = ''
    document.getElementById("runEndLoc").value = ''
    document.getElementById("runDeleteID").value = ''
    document.getElementById("runDate").value = ''
    document.getElementById("runVehicleID").selectedIndex = -1
    document.getElementById("runDriverID").selectedIndex = -1
  }
  else
  {
    var url="travelArrangement_ajax.php"
    url=url+"?rid="+str
    url=url+"&sid="+Math.random()
    xmlHttp.onreadystatechange=runChanged
    xmlHttp.open("GET",url,true)
    xmlHttp.send(null)
  }
}
else if (id == "addRun")
{
    var url="travelArrangement_ajax.php"
    url=url+"?arid="+str
    url=url+"&sid="+Math.random()
    xmlHttp.onreadystatechange=addRun
    xmlHttp.open("GET",url,true)
    xmlHttp.send(null)
}
}

function stateChanged() 
{ 
if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
 { 
 
 var response = eval('(' + xmlHttp.responseText + ')');
 document.getElementById("driverName").value = response["name"]
 document.getElementById("driverPhone").value = response["phone"]
 document.getElementById("driverDeleteID").value = response["ID"]
 } 
}

function stateChanged2() 
{ 
if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
 { 
 
 var response = eval('(' + xmlHttp.responseText + ')');
 document.getElementById("vehicleName").value = response["vehicleName"]
 document.getElementById("vehicleNumPassenger").value = response["numPassenger"]
 document.getElementById("vehicleDeleteID").value = response["ID"]
 } 
}

function runChanged() 
{ 
if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
 { 
 
 var response = eval('(' + xmlHttp.responseText + ')');
 document.getElementById("runTime").innerHTML = response["runTime"]
 document.getElementById("runName").value = response["name"]
 document.getElementById("runStartLoc").value = response["startLoc"]
 document.getElementById("runEndLoc").value = response["endLoc"]
 document.getElementById("runDeleteID").value = response["ID"]
 document.getElementById("runDate").value = response["runDate"]
 document.getElementById("runVehicleID").value = response["vehicleID"]
 document.getElementById("driverDiv").innerHTML = response["driverID"]
 } 
}

function addRun()
{
if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
 { 
 var response = eval('(' + xmlHttp.responseText + ')');
 document.getElementById("assignedDiv").innerHTML = response["assignedSelect"]
 document.getElementById("hiddenRunID").value = response["ID"]
 }
}


function GetXmlHttpObject()
{
var xmlHttp=null;
try
 {
 // Firefox, Opera 8.0+, Safari
 xmlHttp=new XMLHttpRequest();
 }
catch (e)
 {
 //Internet Explorer
 try
  {
  xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
  }
 catch (e)
  {
  xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
 }
return xmlHttp;
}