function get_section_data(elem){
  elem = $(elem)
  // Extract instructions and section type
  const instructions = elem.find("[name='section_instructions']").val()
  const section_id = elem.find("input[name=section_id]").val()
  const section_type = elem.find("select[name=section_type]").val()

  let questions = []
  $.each(elem.find("[name='exam_question']"), function(e, v){
    questions.push(get_question_data(v));
  })
  return {
    instructions,
    section_id,
    section_type,
    questions
  }
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
    console.log(rtn_data);

    $.ajax({
      type: 'POST',
      url: window.location.pathname,
      data: JSON.stringify(rtn_data),
      success: function (data, status, jqXHR) {
        if(data.ok) {
          window.location = SUCCESS_URL || window.location;
        } else {
          // TODO - Show error message to user
          console.log(data.msg);
        }
      },
      error: function (jqXHR, textStatus, errorThrown ) {
      }
    })
  });
});