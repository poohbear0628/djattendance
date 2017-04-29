//See see-charts-init.js for example

//$("#exam-submit").o
$(document).ready(function() {
    $("#exam-submit").click(function (event) {
        event.preventDefault();
        //var questionFormContainer = document.getElementsByClassName("question-form-container");
        //var essaySections = questionFormContainer.querySelectorAll('#essay-question-template');
        //var formEssay = $(essaySections[0]).find('.form-horizontal');
        //var firstEssaySectionExample = essaySections[0].querySelectorAll('.form-horizontal')[0];
        var form_data = $('#surveyForm').serializeArray()
        //var question_data = $('.form-horizontal').serialize();
        var question_data = $('.form-horizontal[name=exam_question]');
        //var question_data = document.getElementsByName('exam_metadata');
        //var question_data = document.forms['.form-horizontal'].elements['.form-group'].value;
        //console.log(form_data);
        console.log(question_data);
        // console.log(data);
        var data = {};
        var question_string = "";
        for(var i=0; i<form_data.length; i++){
            var input = form_data[i];
            if (input.name.equals("question-point") && question_string.equals("")) {
                question_string = "question-point:" + question
            } 
            data[input.name] = input.value;
            console.log(input.name + ": " + input.value);
        }
        console.log(data);
        $.ajax({
            type: 'POST',
            data: data,
            success: function (data, status, jqXHR) {
            },
            error: function (jqXHR, textStatus, errorThrown ) {
              console.log('Exam create save post error!');
              console.log(jqXHR, textStatus, errorThrown);
            }
        })
    });
});