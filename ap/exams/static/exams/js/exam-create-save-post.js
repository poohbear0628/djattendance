//See see-charts-init.js for example

function get_section_data(elem){
    var obj = {};
    elem = $(elem);
    // Extract instructions and section type
    var instructions = elem.find("[name='section_instructions']").val();
    obj.instructions = instructions;
    obj.section_id = elem.find("input[name=section_id]").val();

    obj.questions = [];
    $.each(elem.find("[name='exam_question']"), function(e, v){
        obj.questions.push(get_question_data(v));
    });
    console.log("SECTION DATA: ");
    console.log(obj);
    return obj;
}

function get_question_data(elem){
    var obj = {};
    // Extract question data
    elem = $(elem);
    var container = elem.clone();
    var question_data = $('<form>').append(container).serializeArray();
    for(var i=0; i<question_data.length; i++){
        var key = question_data[i].name;
        var val = question_data[i].value;
        obj[key] = val;
        obj.section_id = elem.find("input[name=question_id]").val();
    }
    console.log("QUESTION DATA: ");
    console.log(obj);
    return obj;
}

//$("#exam-submit").o
$(document).ready(function() {
    $("#exam-submit").click(function (event) {
        event.preventDefault();
        var form_data = $('#surveyForm').serializeArray();
        var question_data = $('.form-horizontal[name=exam_question]');
        var exam_metadata = $('.form-group[name=exam_metadata]');
        //console.log("original metadata: ");
        //console.log(exam_metadata);
        var metadata_container = $(exam_metadata).clone();
        var metadata = $('<form>').append(metadata_container).serializeArray();
        var DELIMITER = "|";
        var section_arr = [];
        var str_data = "";


        // for (var i = 0, len = question_data.length; i < len; i++) {
        //     var container = $(question_data[i]).clone();
        //     //var data = $('<form>').append(container).serializeArray();
        //     var data = $('<form>').append(container).serializeArray();
        //     var section_data = {};
        //     for(var i=0; i<data.length; i++){
        //         section_data[data[i].name] = 
        //     }
        //     section_arr.push(section_data);
        //     if (str_data === "" && !data.includes("question-point=&") ) {
        //         str_data = str_data.concat(data);
        //     } else {
        //         if (!data.includes("question-point=&")) {
        //             str_data = str_data.concat(DELIMITER,data);
        //         }
        //     }

        // }
        
        // console.log(str_data)
        // var sections_array = str_data.split('|');
        var rtn_data = {};
        // Add metadata
        var mtd = {};
        for(var i=0; i<metadata.length; i++){
            mtd[metadata[i].name] = metadata[i].value;
        }
        mtd['training-class'] = $("#selectclass").val();
        mtd['term'] = $("#selectterm").val();
        rtn_data['metadata'] = mtd;

        rtn_data.sections = [];
        // Get section data for each section
        $.each($('.section'), function (e, v){
            var section_data = get_section_data(v);
            if (section_data['questions'].length !== 0) {
                rtn_data.sections.push(section_data);
            }
        });


        // var SECTION_NUM = 0;
        // for(var i=0; i<sections_array.length; i++) {
        //     var question_point;
        //     var question_fields = sections_array[i].split('&');
        //     rtn_data[SECTION_NUM] = {};
        //     for (var j=0; j<question_fields.length; j++) {
        //         console.log(question_fields[j]);
        //         if (question_fields[j] === "A=" || question_fields[j] === "B=" 
        //             || question_fields[j] === "C=" || question_fields[j] === "D=" || question_fields[j] === "E=") {
        //             rtn_data[SECTION_NUM]['mc-answer'] = question_fields[j].charAt(0);
        //         } else {
        //             rtn_data[SECTION_NUM][question_fields[j].split('=')[0]] = question_fields[j].split('=')[1];
        //         }
        //     }

        //     SECTION_NUM = SECTION_NUM + 1;
        // }

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
        console.log('RETURN DATA IS:');
        console.log(rtn_data);
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