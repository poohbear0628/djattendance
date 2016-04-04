function render_question(question_json, response_json, display_type, index){
    var question = JSON.parse(question_json);
    var response = JSON.parse(response_json);
    if (question.type == "essay")
        render_essay_question(question, response, display_type, index);
    else
        alert("Question type not yet implemented!")
}

function render_essay_question(question, response, display_type, index){
    // Is this better than just using document.write() for all of this?
    var ol = document.getElementById("ol");

    // Question String
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(question.prompt));
    var pts = document.createElement("b");
    pts.innerHTML = " (Points: " + question.points + ")";
    li.appendChild(pts);
    ol.appendChild(li);
    var br = document.createElement("br");
    ol.appendChild(br);

    // Response area
    var resp_area = document.createElement("textarea");
    resp_area.value = response.response;
    resp_area.className = "exam-response";
    resp_area.id = index;
    resp_area.setAttribute("disabled", display_type == "Grade");
    resp_area.setAttribute("cols", "100");
    resp_area.setAttribute("rows", "10");
    resp_area.setAttribute("placeholder", "Type your response here.");
    resp_area.setAttribute("name", "response");
    ol.appendChild(resp_area);
    br = document.createElement("br");
    ol.appendChild(br);

    // Word count
    if (display_type == "Grade" || display_type == "Retake"){
        var wc_text = document.createElement("b");
        wc_text.innerHTML = "Word Count: ";
        ol.appendChild(wc_text)
        var wc_span = document.createElement("span");
        wc_span.id = "count" + index;
        wc_span.innerHTML = "0";
        ol.appendChild(wc_span);
        br = document.createElement("br");
        ol.appendChild(br);
    }

    // Score and Grader Comment
    if (display_type == "Grade" || display_type == "Retake"){
        var score_text = document.createElement("b");
        score_text.innerHTML = "Score: ";
        ol.appendChild(score_text);
        var score_input = document.createElement("input");
        score_input.id = "score" + index;
        score_input.className = "score form-control";
        score_input.type = "text";
        score_input.value = response.score;
        score_input.setAttribute("name", "question-score");
        if (display_type != "Grade")
            score_input.setAttribute("disabled", true);
        ol.appendChild(score_input);

        var comment_text = document.createElement("b");
        comment_text.innerHTML = " Comment: ";
        ol.appendChild(comment_text);
        var comment_input = document.createElement("input");
        comment_input.id = "comment" + index;
        comment_input.className = "grader-comment form-control";
        comment_input.type = "text";
        comment_input.value = response.comment;
        comment_input.setAttribute("name", "grader-comment");
        if (display_type != "Grade")
            comment_input.setAttribute("disabled", true);
        ol.appendChild(comment_input);

        br = document.createElement("br");
    }
}