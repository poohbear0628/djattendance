
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
  //console.log("SECTION DATA: ");
  console.log(obj);
  return obj;
}

function get_question_data(elem){
  var obj = {};
  // Extract question data
  elem = $(elem);
  console.log(elem);
  var container = elem.clone();
  var question_data = $('<form>').append(container).serializeArray();
  for(var i=0; i<question_data.length; i++){
    var key = question_data[i].name;
    var val = question_data[i].value;
    obj[key] = val;
    obj.section_id = elem.find("input[name=question_id]").val();
  }
  if(obj["question-type"] == "tf"){
    obj["answer"] = elem.find("label.active input").val();
  }
  //console.log("QUESTION DATA: ");
  return obj;
}

function getCookie(name)
{
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?

      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(document).ready(function() {
  $("#exam-submit").click(function (event) {
    event.preventDefault();
    var rtn_data = {};

    // Add exam metadata
    var exam_metadata = $('.form-horizontal[name=exam_metadata]');
    var metadata_container = $(exam_metadata).clone();
    var metadata = $('<form>').append(metadata_container).serializeArray();

    var mtd = {};
    for(var i=0; i<metadata.length; i++){
      mtd[metadata[i].name] = metadata[i].value;
    }
    mtd['training_class'] = $("#id_training_class").val();
    rtn_data['metadata'] = mtd;

    var question_data = $('.form-horizontal[name=exam_question]');
    rtn_data.sections = [];
    // Get section data for each section
    $.each($('.section'), function (e, v){
      var section_data = get_section_data(v);
      if (section_data['questions'].length !== 0) {
        rtn_data.sections.push(section_data);
      }
    });

    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    });
    $.ajax({
      type: 'POST',
      data: JSON.stringify(rtn_data),
      success: function (data, status, jqXHR) {
        window.location = SUCCESS_URL || window.location;
      },
      error: function (jqXHR, textStatus, errorThrown ) {
        console.log('Exam create save post error!');
        console.log(jqXHR, textStatus, errorThrown);
      }
    })
  });
});