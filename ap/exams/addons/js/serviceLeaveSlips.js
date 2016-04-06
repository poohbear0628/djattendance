/* Matthew Hsieh
*
* serviceLeaveSlips javascript
*
*/

function showLayer(id)
{
//alert(id);
var element = document.getElementById(id + 'id');
//alert(element);
var index = element.options.selectedIndex;
var box = document.getElementById(id + 'div');
var auto = document.getElementById(id + '_autocomplete');
var text = document.getElementById(id);
if (index == 2 || index == 3)
{
box.style.visibility = 'visible';
}
else if (index == 0 || index == 1 || index == 4)
{
box.style.visibility = 'hidden';
text.value = "";
auto.value = "";
}
}


function getElementsByStyleClass (className) {
  var all = document.all ? document.all :
    document.getElementsByTagName('*');
  var elements = new Array();
  for (var e = 0; e < all.length; e++)
    if (all[e].className == className)
      elements[elements.length] = all[e];
  return elements;
}

function checkValues()
{
var returnval = true;
var element = getElementsByStyleClass('divID');
var formIDs = document.getElementsByName('formID');
for (var j = 0; j < formIDs.length; j++)
{
formIDs[j].value
}
for (var i = 0; i < element.length; i++)
{
  if (element[i].childNodes[0].value)
  {
    if (element[i].childNodes[1].value)
    {
    }
    else
    {
    alert(element[i].childNodes[0].value + ' is not a valid name.');
    returnval = false;
    }
    for (var j = 0; j < formIDs.length; j++)
    {
      if (element[i].childNodes[1].value == formIDs[j].value)
        {
        alert('There is a duplicate name.');
        returnval = false;
        }
    }
    
  }
}



if (returnval == true)
{
submitForm();
}
return returnval;
}

function submitForm()
{
var element = document.getElementsByName('serviceLeaveSlipForm');
var button = document.getElementById('submitForm');
button.type = 'submit';
element.submit;
}

function addNewTrainees()
{
var traineeID = document.getElementById('newTrainee');
var innerDiv = document.getElementById('traineeDiv');
var templateRow = document.getElementById('templateRow');

}

function updateName(name)
{
if (name == "*")
{ return 'Star'; }
if (name == "S")
{ return 'Sister'; }
if (name == "B")
{ return 'Brother'; }
if (name == "RetB")
{ return 'Returning Brother'; }
if (name == "RetS")
{ return 'Returning Sister'; }

}



