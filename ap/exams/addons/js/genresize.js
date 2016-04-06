/////////////////////////////////////////////////////////////////////////
// Generic Resize by Erik Arvidsson {MODIFIED}                         //
//                                                                     //
// You may use this script as long as this disclaimer is remained.     //
// See www.dtek.chalmers.se/~d96erik/dhtml/ for mor info               //
//                                                                     //
// How to use this script!                                             //
// Link the script in the HEAD and create a container (DIV, preferable //
// absolute positioned) and add the class="resizeMe" to it.            //
/////////////////////////////////////////////////////////////////////////

var theobject = null; //This gets a value as soon as a resize start

function resizeObject()
{
	this.el = null; // pointer to the object
	this.dir = ""; // type of current resize (n, s, e, w, ne, nw, se, sw)
	this.grabx = null; // Some useful values
	this.graby = null;
	this.width = null;
	this.height = null;
	this.left = null;
	this.top = null;
}

function clientX(event, el)
{
	if (document.all) // For IE
		return event.offsetX + el.clientTop;

	// For Firefox
	return event.pageX - el.offsetLeft;
}

function clientY(event, el)
{
	if (document.all) // For IE
		return event.offsetY + el.clientTop;

	// For Firefox
	return event.pageY - el.offsetTop;
}

//Find out what kind of resize! Return a string inlcluding the directions
function getDirection(el, event)
{
	var dir = "";
	var xPos = clientX(event, el);
	var yPos = clientY(event, el);
	var width = el.offsetWidth;
	var height = el.offsetHeight;
	var offset = 8; // The distance from the edge in pixels

	if (yPos < offset)
		dir += "n";
	else if (yPos > height - offset)
		dir += "s";

	if (xPos < offset)
		dir += "w";
	else if (xPos > width - offset)
		dir += "e";

	return dir;
}

function doDown(event)
{
	if (!event)
		event = window.event;

	var el;
	
	if (!event.srcElement)
		el = event.target;
	else
		el = event.srcElement;

	if (el == null || el.className != "resizeMe")
	{
		theobject = null;
		return;
	}		

	dir = getDirection(el, event);

	if (dir == "")
		return;

	if (document.all) // For IE
	{
	    width = el.offsetWidth;
	    height = el.offsetHeight;
	}
	else // For Firefox
	{
	    width = document.defaultView.getComputedStyle(el, null).getPropertyValue("width").replace("px", "") * 1;
	    height = document.defaultView.getComputedStyle(el, null).getPropertyValue("height").replace("px", "") * 1;
	}

	theobject = new resizeObject();
	theobject.el = el;
	theobject.dir = dir;
	theobject.grabx = event.pageX;
	theobject.graby = event.pageY;
	theobject.width = width;
	theobject.height = height;
	theobject.left = el.offsetLeft;
	theobject.top = el.offsetTop;

	event.returnValue = false;
	event.cancelBubble = true;
}

function doUp(event)
{
	if (theobject != null)
		theobject = null;
}

function doMove(event)
{
	if (!event)
		event = window.event;
		
	var el;

	if (!event.srcElement)
		el = event.target;
	else
		el = event.srcElement;

	if (el.className == "resizeMe")
	{
		var str = getDirection(el, event);

		// Fix the cursor
		if (str == "")
			str = "default";
		else
			str += "-resize";
			
		el.style.cursor = str;
	}

	// Dragging starts here
	if (theobject != null)
	{
		var xMin = 8; // The smallest width possible
		var yMin = 8; // The smallest height possible
		var xPos = event.pageX;
		var yPos = event.pageY;
		var xDiff = xPos - theobject.grabx;
		var yDiff = yPos - theobject.graby;

//	alert("x = " + xPos + "\ny = " + yPos + "\nw = " + theobject.width + "\nh = " + theobject.height + "\ngx = " + theobject.grabx + "\ngy = " + theobject.graby)

		if (dir.indexOf("e") != -1)
			theobject.el.style.width = Math.max(xMin, theobject.width + xDiff) + "px";
	
		if (dir.indexOf("s") != -1)
			theobject.el.style.height = Math.max(yMin, theobject.height + yDiff) + "px";

		if (dir.indexOf("w") != -1)
		{
			theobject.el.style.left = (theobject.left + xDiff) + "px";
			theobject.el.style.width = Math.max(xMin, theobject.width - xDiff) + "px";
		}
		
		if (dir.indexOf("n") != -1)
		{
			theobject.el.style.top = (theobject.top + yDiff) + "px";
			theobject.el.style.height = Math.max(yMin, theobject.height - yDiff) + "px";
		}

		event.returnValue = false;
		event.cancelBubble = true;
	} 
}

dojo.event.connect(document, "onmousedown", doDown);
dojo.event.connect(document, "onmouseup", doUp);
dojo.event.connect(document, "onmousemove", doMove);
