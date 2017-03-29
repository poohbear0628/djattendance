$("#exam-submit").submit(function (event) {
    console.log("what");
    event.preventDefault();
    //var questionFormContainer = document.getElementsByClassName("question-form-container");
    //var essaySections = questionFormContainer.querySelectorAll('#essay-question-template');
    //var formEssay = $(essaySections[0]).find('.form-horizontal');
    //var firstEssaySectionExample = essaySections[0].querySelectorAll('.form-horizontal')[0];
    var formGroups = $('.form-group').serializeArray();
    console.log(formGroups);

    if (seats.grid.length > 0) {
      var chart = {
        name: $("#chart-name").val(),
        desc: '',
        width: $("#width").val(),
        height: $("#height").val(),
        trainees: seats.grid,
      }

      if (chartId) {
        chart.id = chartId;
      }

      $.ajax({
        url: '/api/charts/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(chart),
        success: function (data, status, jqXHR) {
          $("#chart-submit-error").hide();
          $("#chart-submit-success").show();
          if (!chartId) {
            window.location.href = menuUrl;
          }
          setTimeout(function() {
            $("#chart-submit-success").slideUp(1000)
          }, 5000);
        },
        error: function (jqXHR, textStatus, errorThrown ) {
          console.log('Chart post error!');
          console.log(jqXHR, textStatus, errorThrown);
          $("#chart-submit-error").show();
          $("#chart-submit-error").empty();
          $("#chart-submit-error").append('Error! ' + errorThrown);
        }
      })
    }
  });