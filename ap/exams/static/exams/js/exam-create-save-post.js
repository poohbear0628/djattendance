//See see-charts-init.js for example

//$("#exam-submit").o
$(document).ready(function() {
    $("#exam-submit").click(function (event) {
        event.preventDefault();
        var form_data = $('#surveyForm').serializeArray();
        var question_data = $('.form-horizontal[name=exam_question]');
        var exam_metadata = $('.form-group[name=exam_metadata]');
        var metadata_container = $(exam_metadata).clone();
        var metadata = $('<form>').append(metadata_container).serializeArray();
        var DELIMITER = "|";
        var str_data = "";
        for (var i = 0, len = question_data.length; i < len; i++) {
            var container = $(question_data[i]).clone();
            //var data = $('<form>').append(container).serializeArray();
            var data = $('<form>').append(container).serialize();

            if (str_data === "" && !data.includes("question-point=&") ) {
                str_data = str_data.concat(data);
            } else {
                if (!data.includes("question-point=&")) {
                    str_data = str_data.concat(DELIMITER,data);
                }
            }

        }
        
        console.log(str_data)
        var sections_array = str_data.split('|');
        var rtn_data = {};
        rtn_data['metadata'] = metadata;
        var SECTION_NUM = 0;
        for(var i=0; i<sections_array.length; i++) {
            var question_point;
            var question_fields = sections_array[i].split('&');
            rtn_data[SECTION_NUM] = {};
            for (var j=0; j<question_fields.length; j++) {
                console.log(question_fields[j]);
                if (question_fields[j] === "A=" || question_fields[j] === "B=" 
                    || question_fields[j] === "C=" || question_fields[j] === "D=" || question_fields[j] === "E=") {
                    rtn_data[SECTION_NUM]['mc-answer'] = question_fields[j].charAt(0);
                } else {
                    rtn_data[SECTION_NUM][question_fields[j].split('=')[0]] = question_fields[j].split('=')[1];
                }
            }

            SECTION_NUM = SECTION_NUM + 1;
        }

        /**for(var i=0; i<form_data.length; i++){
            var input = form_data[i];
            if (input.name.equals("question-point") && question_string.equals("")) {
                question_string = "question-point:" + question
            } 
            data[input.name] = input.value;
            console.log(input.name + ": " + input.value);
        }
        */
        //console.log(data);
        $.ajax({
            type: 'POST',
            data: JSON.stringify(rtn_data),
            success: function (data, status, jqXHR) {
            },
            error: function (jqXHR, textStatus, errorThrown ) {
              console.log('Exam create save post error!');
              console.log(jqXHR, textStatus, errorThrown);
            }
        })
    });
});