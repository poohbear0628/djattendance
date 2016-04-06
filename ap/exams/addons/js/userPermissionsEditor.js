// JavaScript Document
var id_array = new Array();
var class_array = new Array();
var name_array = new Array();

var getElementsByClassName = function (className, tag, elm){
	if (document.getElementsByClassName) {
		getElementsByClassName = function (className, tag, elm) {
			elm = elm || document;
			var elements = elm.getElementsByClassName(className),
				nodeName = (tag)? new RegExp("\\b" + tag + "\\b", "i") : null,
				returnElements = [],
				current;
			for(var i=0, il=elements.length; i<il; i+=1){
				current = elements[i];
				if(!nodeName || nodeName.test(current.nodeName)) {
					returnElements.push(current);
				}
			}
			return returnElements;
		};
	}
	else if (document.evaluate) {
		getElementsByClassName = function (className, tag, elm) {
			tag = tag || "*";
			elm = elm || document;
			var classes = className.split(" "),
				classesToCheck = "",
				xhtmlNamespace = "http://www.w3.org/1999/xhtml",
				namespaceResolver = (document.documentElement.namespaceURI === xhtmlNamespace)? xhtmlNamespace : null,
				returnElements = [],
				elements,
				node;
			for(var j=0, jl=classes.length; j<jl; j+=1){
				classesToCheck += "[contains(concat(' ', @class, ' '), ' " + classes[j] + " ')]";
			}
			try	{
				elements = document.evaluate(".//" + tag + classesToCheck, elm, namespaceResolver, 0, null);
			}
			catch (e) {
				elements = document.evaluate(".//" + tag + classesToCheck, elm, null, 0, null);
			}
			while ((node = elements.iterateNext())) {
				returnElements.push(node);
			}
			return returnElements;
		};
	}
	else {
		getElementsByClassName = function (className, tag, elm) {
			tag = tag || "*";
			elm = elm || document;
			var classes = className.split(" "),
				classesToCheck = [],
				elements = (tag === "*" && elm.all)? elm.all : elm.getElementsByTagName(tag),
				current,
				returnElements = [],
				match;
			for(var k=0, kl=classes.length; k<kl; k+=1){
				classesToCheck.push(new RegExp("(^|\\s)" + classes[k] + "(\\s|$)"));
			}
			for(var l=0, ll=elements.length; l<ll; l+=1){
				current = elements[l];
				match = false;
				for(var m=0, ml=classesToCheck.length; m<ml; m+=1){
					match = classesToCheck[m].test(current.className);
					if (!match) {
						break;
					}
				}
				if (match) {
					returnElements.push(current);
				}
			}
			return returnElements;
		};
	}
	return getElementsByClassName(className, tag, elm);
};

//displays the correct trainees with overlapping classes
function displayID(class_checked)
{
//first hide all elements of other ids
  for (var j = 0; j < class_array.length; j++)
  {
  hideID(class_array[j]);
  }
  //get element by id
  //loop through all the class items
  for (var i = 0 ; i < id_array.length; i++)
  {
  var el = document.getElementById(class_checked + "_" + id_array[i]);
  el.style.display = "";
  }
  //add class_checked to class_array
  class_array[class_array.length] = class_checked; 
}

//hides table rows by class
function hideID(value)
{
  var elements = getElementsByClassName(value);
  for (var i = 0 ; i < elements.length; i++)
  {
    elements[i].style.display = "none";
  } 
}

//gets ID array of trainees based on class
function getIDarray(value)
{
var tempArray = new Array();
var el = getElementsByClassName(value);
  for (var i = 0; i < el.length; i++)
    {
    var index = el[i].id.indexOf('_') + 1;
    tempArray[i] = el[i].id.substring(index);
  }
return tempArray;
}

function addName()
{
  var id = document.getElementById('selectedValues');
  id.innerHTML = "Categories: ";
  for (var i=0; i < name_array.length; i++)
  {
  id.innerHTML += name_array[i] + "-"; 
  }
}


//
function addID(checkbox, value, name)
{
  //see if box is checked or unchecked
  //alert(value + name);
  //if checked, displayID
  if(checkbox.checked == true) 
  {
  var tempArray = new Array();
  var newArray = new Array();
  //add traineeID
  tempArray = getIDarray(value);
  //add name to array
  name_array.push(name); 
    if (id_array.length == 0) //empty
    {
  //set temp array to new array
    id_array = tempArray;
    }
    else
    { //not empty, check for duplicates
    var counter = 0;
    for (var j = 0; j < tempArray.length; j++)
      {
      for (var i = 0; i < id_array.length; i++)
        { //loop through id_array and check if that traineeID exists
          if (tempArray[j] == id_array[i])
            { //if there is a match, keep this ID in temp array
            newArray[counter] = id_array[i];
            counter++;
            }
        }
      }
    //clear and set id_array to this new array
    id_array = newArray; 
    }
    addName();
    displayID(value);
  }
  //if not checked, have a way to display to right trainees
  else { 
  //remove from name array
  for (var i = 0; i < name_array.length; i++)
  {
    if (name_array[i] == name)
    {
    name_array.splice(i, 1);
    }
  }
  
  //first remove an class from class_array (is there a pop function or a remove from array function?)
  for (var i = 0; i < class_array.length; i++)
  {
    if (class_array[i] == value) //found the value
    {
    //remove the value
    class_array.splice(i, 1); //this will remove that value
    }
  }
  
  //first we know the last value in the array is the one visible
  //just use length to get last element
  var lastElement = class_array[class_array.length-1]; //last element in the array
  //we need to get the right traineeID's in the array
  var matchingArray = new Array();
  if (class_array.length == 0)
  {
  id_array = null;
  hideID(value)
  } 
  if (class_array.length == 1)
  {
  id_array = getIDarray(class_array[0]);
  }
  else
  {
  for (var i = 0; i < class_array.length; i++)
  {
  //for every element in the class_array, we need to make a list of matching elements
  var arrayOne = getIDarray(class_array[i]); //this is an array of IDs for this class
  if (matchingArray.length != 0)
  {
    var tempArray = new Array();
    var counter = 0;
    for (var k = 0; k < matchingArray.length; k++)
    {
      for (var j = 0; j < arrayOne.length; j++)
      { 
      if (matchingArray[k] == arrayOne[j]) //looks at matches
        {
        tempArray[counter] = arrayOne[j]; //adds matches to mathcing array.
        counter++;
        }
      }
      
    }
    matchingArray = tempArray;
  }
  else
  {
  matchingArray = tempArray;
  } 
  }
  }
  id_array = matchingArray;
  //we need to add the matching ID's of the the classes remaining that do not already exist
  
  //if this one is unchecked then
    addName();
    displayID(lastElement); 
  }
  
}

function confirmDelete()
	{
		var isDelete = confirm ("You are about to delete permissions for the selected users, are you sure you want to continue?")
		if (!isDelete)
			document.userPermissionsEditor.command.value="cancel";
		else
		{
			document.userPermissionsEditor.command.value="delete";
			document.userPermissionsEditor.submit();
		}
	}