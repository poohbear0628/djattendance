var xmlHttp

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


function getDate(str, row)
{
xmlHttp2=GetXmlHttpObject()
if (xmlHttp2==null)
 {
 alert ("Browser does not support HTTP Request")
 return
 }

className = str.id.split("_")[0]
classID = str.id.split("_")[1]
name = className + "_" + classID;
dateID = document.getElementById(name).value
var url="requestForm_ajax.php"
url=url+"?dateID="+dateID
url=url+"&row="+row
url=url+"&sid="+Math.random()
xmlHttp2.onreadystatechange=stateChanged2
xmlHttp2.open("GET",url,true)
xmlHttp2.send(null)
}

function clearRow(value)
{
document.getElementById("div_" + value).innerHTML = "";
document.getElementById("list_" + value).value = "";
}


function stateChanged2() 
{ 
if (xmlHttp2.readyState==4 || xmlHttp2.readyState=="complete")
 { 
 
 var response = eval('(' + xmlHttp2.responseText + ')');
 row = response["row"];
 document.getElementById(row).innerHTML = response["html"];
 } 
}



