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
    resp_area.value = response.response == null ? "" : response.response;
    resp_area.className = "exam-response";
    resp_area.id = index;
    if (display_type != "Take" && display_type != "Retake")
        resp_area.setAttribute("disabled", true);
    resp_area.setAttribute("cols", "100");
    resp_area.setAttribute("rows", "10");
    resp_area.setAttribute("placeholder", "Type your response here.");
    resp_area.setAttribute("name", "response");
    ol.appendChild(resp_area);
    br = document.createElement("br");
    ol.appendChild(br);

    // Word count
    var wc_text = document.createElement("b");
    wc_text.innerHTML = "Word Count: ";
    ol.appendChild(wc_text)
    var wc_span = document.createElement("span");
    wc_span.id = "count" + index;
    wc_span.innerHTML = "0";
    ol.appendChild(wc_span);
    br = document.createElement("br");
    ol.appendChild(br);

    Countable.live(resp_area, function(counter){
        var span = document.getElementById("count" + index);
        span.innerHTML = counter.words;
    })

    // Score and Grader Comment
    if (display_type == "Grade" || display_type == "Retake"){
        var score_text = document.createElement("b");
        score_text.innerHTML = "Score: ";
        ol.appendChild(score_text);
        var score_input = document.createElement("input");
        score_input.id = "score" + index;
        score_input.className = "score form-control";
        score_input.type = "text";
        score_input.value = response.score == null ? "" : response.score;
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
        comment_input.value = response.comment == null ? "" : response.comment;
        comment_input.setAttribute("name", "grader-comment");
        if (display_type != "Grade")
            comment_input.setAttribute("disabled", true);
        ol.appendChild(comment_input);

        br = document.createElement("br");
    }
}

 function render_question_for_edit(question_json, index){
    var question = JSON.parse(question_json);
    if (question.type == "essay")
        render_essay_question_for_edit(question, index);
    else
        alert("Question type not yet implemented!")
}

function render_essay_question_for_edit(question, index){
    var ol = document.getElementById("qBox");

    var newDiv = document.createElement("div");
    // Question String
    var question_prompt = document.createElement("input");
    question_prompt.id = "question" + index;
    question_prompt.className = "question form-control";
    question_prompt.type = "text";
    question_prompt.value = question.prompt;
    question_prompt.setAttribute("name", "question-prompt");
    newDiv.appendChild(question_prompt);
    var question_point = document.createElement("input");
    question_point.id = "qpoint" + index;
    question_point.className = "question form-control";
    question_point.type = "text";
    question_point.value = question.points;
    question_point.setAttribute("name", "question-point");
    newDiv.appendChild(question_point);

    //Create array of question types
    var array = ["Essay"];

    //Create and append select list
    var question_type = document.createElement("select");
    question_type.id = "selectbasic" + index;
    question_type.className = "question form-control";
    question_type.setAttribute("name", "question-type");
    newDiv.appendChild(question_type);
    //Create and append the options
    for (var i = 0; i < array.length; i++) {
        var option = document.createElement("option");
        option.value = array[i].toLowerCase();
        option.text = array[i];
        if (question_type == option.value) {
            option.selected="selected"
        }
        question_type.appendChild(option);
    }
    var remove_button = document.createElement("input");
    remove_button.id = index;
    remove_button.type = "button";
    remove_button.value = "Remove question";
    remove_button.className = "remove btn btn-info-outline";
    newDiv.appendChild(remove_button);

    var br = document.createElement("br");
    newDiv.appendChild(br);
    var br2 = document.createElement("br");
    newDiv.appendChild(br2);

    ol.appendChild(newDiv);
}

function package_questions(display_type){
    var question_count = document.getElementById("question_count").getAttribute("value");
    for (i = 0; i < question_count; i++){
        var question = JSON.parse(document.getElementById("question_" + (i+1).toString()).getAttribute("value"));
        var response = JSON.parse(document.getElementById("response_" + (i+1).toString()).getAttribute("value"));

        if (question.type == "essay")
            package_essay_question(response, display_type, i+1);
        else
            alert("Question type not yet implemented!")
    }
}

function package_essay_question(response, display_type, index){
    var form = document.getElementById("exam_form");
    
    if (display_type == "Take" || display_type == "Retake"){
        response.response = document.getElementById(index).value;
    }

    if (display_type == "Grade"){
        response.score = document.getElementById("score" + index).value;
        response.comment = document.getElementById("comment" + index).value;
    }

    var input_field = document.createElement("input");
    input_field.setAttribute("type", "hidden");
    input_field.setAttribute("name", "response_json");
    input_field.setAttribute("value", JSON.stringify(response));

    form.appendChild(input_field);
}