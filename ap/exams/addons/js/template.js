//create template to add information for floating data entry
function createTemplate()
{
  var template = dojo.html.createNodesFromText(
  '<div id="template" class="resizeMe">\n' +
  '	<a href="javascript:templateHide()" style="position:absolute; top:2px; right:10px">Close Window</a>\n' +
  '<table>\n' +
  '		<tr>\n' +
  '			<td>\n' +
  '				<div id="templateOne">\n' +
  '				</div>\n' +
  '			</td>\n' +
  '	  </tr>\n' +
  '	</table>\n' +
  '</div>', true)[0];
  
  dojo.body().appendChild(template);
  
}

function templateShow(object)
{
dojo.io.bind(
	{
		url: fttaUrl("/home.php"),
		method: "post",
		content:
		{
		    action:"show",

		},
		mimetype: "text/json",
		load:
			function(type, data, xhr)
			{

				//////////////////////////////////
				// Display the trainee selector //
				//////////////////////////////////

				var ts = document.getElementById("template");
				
				if (document.all) // For IE
				{
					ts.style.top = document.body.scrollTop + 10;
					ts.style.left = document.body.scrollLeft + 10;
				}
				else // For Firefox
				{
					ts.style.top = window.pageYOffset + object.offsetTop + 50;
					ts.style.left = window.pageXOffset + object.offsetLeft;
				}

				ts.style.display = "block";

			}
	});
}






function templateHide()
{
	document.getElementById("template").style.display = "none";
}


dojo.addOnLoad(
	function()
	{
		createTemplate();
	}
);

