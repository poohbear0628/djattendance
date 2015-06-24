$(document).ready(function(){
	// counts the number of words in the given text area and updates the
	// displayed word count
	function update_word_count(textarea){
		text = textarea.val();

		// review(haileyl): this regex isn't 100% accurate. Constructions like
		// "word--word" and "test...test" will each only be counted as only
		// one word.  Do we care?
		matches = text.match(/\S+/g);
		count = matches == null ? 0 : matches.length;

		// span is identified by count#, where # is the question id
		span = document.getElementById("count" + textarea.attr("id"));
		span.innerHTML = count;
	}

	$('textarea').each(function(){
		// update on textarea content change
		$(this).on("input", function() {
			update_word_count($(this));
		});

		// calculate word count on page load
		update_word_count($(this));
	});
});