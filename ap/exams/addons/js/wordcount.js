/*
 * 
 * Textarea Word Count Jquery Plugin 
 * Version 1.1.0
 * 
 * Copyright (c) 2008 Roshan Bhattarai
 * website: http://roshanbh.com.np
 * 
 * Improved by Alan Hogan, 2009.
 * website: http://alanhogan.com 
 * 
 * Improved by Allen Webb, 2011.
 * FTTA
 * 
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 * 
*/

jQuery.fn.wordCount = function(params){
	var ce = this.prev();
	var p = {
		counterElement: ce // this is a jquery element
	};

	if(params) {
		jQuery.extend(p, params);
	}

        this.keyup(function() //moved from keypress to keyup because of browser support issues
	{
                var list = this.value.split(/[\s\.\?\,]+/);
		this.total_words=list.length; //moved the total_words var to "this" so that it could be used in tests outside this .js and added , and added , to the class -Allen W.
                if(this.total_words>1 && list[this.total_words-1]=='') //remove blank last word
                    this.total_words--;
                if(this.total_words>0 && list[0]=='') //remove blank first word
                    this.total_words--;
		p.counterElement.children('b').html(this.total_words);
	});

	//for each keypress function on text areas
	this.keypress(function()
	{
		jQuery(this).keyup();
	});
	this.blur(function()
	{
		jQuery(this).keyup();
	});
	this.focus(function()
	{
		jQuery(this).keyup();
	});
	this.focus();
};
