/* outlineLinks.js
 * create anchors to outline links for page navigation
 * Author: Allen Webb
 */

$(document).ready(function(){
    var nav = $("<div id='nav_float' style='position: fixed; width: 200px; right:0px; top:50px; padding: 5px; background-color: rgba(240,240,240,0.8);'>\n\
<div id='toggle'><a href='javascript:void(0);'>Show / Hide</a></div></div>");
    nav.find('#toggle').click(function(){
        $(this).parent().children().not(this).slideToggle('fast');
    });
    var stack = [['',$('<ul><ul>').appendTo(nav)]];
    $('#content h1').add('#content h2').add('#content h3').add('#content h4').each(function(){
        while(stack.length>0 && this.nodeName<=stack[stack.length-1][0])
            stack.pop();
        var header = $(this);
        var header_text = header.html().replace(/<[^>]+>/g,'');
        var header_name = header_text.replace(/\s+/g,'_');
        header.before('<a name="'+header_name+'"></a>');
        var listItem = $('<li><a href="#'+header_name+'">'+header_text+'</a><ul><ul><li>');
        stack[stack.length-1][1].append(listItem);
        stack.push([this.nodeName,listItem]);
    });
    nav.appendTo('body');
});