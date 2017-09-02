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
  if(obj["question-type"] == "tf"){
    obj["answer"] = elem.find("label.active input").val();
  }
  return obj;
}

$(function (){
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

    $.ajax({
      type: 'POST',
      url: window.location.pathname,
      data: JSON.stringify(rtn_data),
      success: function (data, status, jqXHR) {
        window.location = SUCCESS_URL || window.location;
      },
      error: function (jqXHR, textStatus, errorThrown ) {
      }
    })
  });
});