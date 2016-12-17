// Creating the seating chart object after loading data

var hide_seats = false;

var scObject = {
  map: seats,
  hideEmptySeats: hide_seats,
  naming: {
    top: true,
    left: true,
  },
  click: function (ev, elem) {
    // var elem = this.settings.$node[0];
    var popover = $(elem).popover({
      placement: 'right auto',
      trigger: 'manual',
      content: '<input class="form-control" placeholder="Trainee name" id="trainee-name"/>',
      html: true
    }).popover('show');

    var seatId = "#" + elem.id;
    var rc_list = elem.id.split('_');
    var row = rc_list[0];
    var column = rc_list[1];

    var input = popover.find("#trainee-name");

  }
};

$(document).ready(function() {
  // Initialize Seating Chart

  sc = $('#seat-map').seatCharts(scObject);
  var w = parseInt($("#width").val());
  var h = parseInt($("#height").val());
  $("#seat-map").css("width", ((w+2)*60).toString() + "px");
  // Popover Logic

  $('body').on('shown.bs.popover', function(e) {
    console.log('popover shown', e);

    var elem = $(e.target);
    var rcpair = elem.attr('id').split('_');
    var row = rcpair[0] - 1;
    var column = rcpair[1] - 1;
    var popover = elem.data('bs.popover').$tip;
    var input = popover.find('input');

    input.on('keydown', function (e) {
      //everything depends on the pressed key
      switch (e.which) {
        //spacebar will just trigger the same event mouse click does
        case 13:
          e.preventDefault();
          console.log('space/enter', e);
          console.log('target value is', e.target.value);
          if (e.target.value == "") {
            traineeList.push({value: seats.grid[row][column].name, id: seats.grid[row][column].pk});
            seats.grid[row][column] = {};
            elem.text("");
          }
          elem.popover('destroy');
          // $(fn.currentCell).mouseup();
          break;
        default:
          break;
      }
    });

    input.autocomplete({
      lookup: traineeList,
      autoSelectFirst: true,
      onSelect: function(selection) {
        console.log('onselect', selection, selection.value, elem);
        elem.text(selection.value);
        var isSeated = traineeList.map(function(x) {return x.id; }).indexOf(selection.id);
        if (isSeated != -1) {
          if (Object.keys(seats.grid[row][column]).length != 0) {
            traineeList.push({value: seats.grid[row][column].name, id: seats.grid[row][column].pk});
            seats.grid[row][column].pk = selection.id;
            seats.grid[row][column].name = selection.value;
            elem.popover('destroy');
            traineeList.splice(isSeated, 1);
          } else {
            seats.grid[row][column].pk = selection.id;
            seats.grid[row][column].name = selection.value;
            elem.popover('destroy');
            //traineeSeated.push({value: selection.value, id: selection.id});
            //delete from traineeList if seated
            traineeList.splice(isSeated, 1);
        }
      }  
        // elem.blur();
      }
    });

    input.focus();
    input.val(elem.text());
    input.select();
  });

  $('body').on('blur', '#trainee-name', function(e) {
    console.log('blur global', e);
    $(e.currentTarget).parent().parent().popover('destroy');
  });


  $("#submit-chart-form").submit(function (event) {
    event.preventDefault();
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

  $("#width-height-form").submit(function (event) {
    event.preventDefault();

    $('#seat-map').empty();

    var w = parseInt($("#width").val());
    var h = parseInt($("#height").val());
    $("#seat-map").css("width", ((w+2)*60).toString() + "px");

    if (seats) {
      seats.setDimensions(w, h);
    } else {
      seats = new Grid(w, h);
    }

    sc = $('#seat-map').seatCharts(scObject);

  });

  $("#chart_preview").click(function (e){
    e.preventDefault();
    hide_seats = !hide_seats;
    scObject.hideEmptySeats = hide_seats;
    $('#seat-map').empty();
    sc = $('#seat-map').seatCharts(scObject);
    var w = parseInt($("#width").val());
    var h = parseInt($("#height").val());
    $("#seat-map").css("width", ((w+2)*60).toString() + "px");
  });

  $("#chart_partition").click(function (e){

  });

});