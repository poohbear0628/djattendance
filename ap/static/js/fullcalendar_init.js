$(document).ready(function() {
  var color_names = {
    "darkslateblue": "483d8b",
    "yellowgreen": "9acd32"
  }

  var color_list = [];

  var NUM_OF_COLORS = 10;

  for (var i=0; i<NUM_OF_COLORS+1; i++) {
    var color = $.xcolor.gradientlevel('darkslateblue', 'yellowgreen', i, NUM_OF_COLORS).getColor();
    color_list.push(color);
  }

  var color_dict = {};

  for (var i=0; i<services.length; i++) {
    var c = services[i].category
    if (!(c in color_dict)) {
      color_dict[c] = color_list.pop();
    }

    services[i]['color'] = color_dict[c];
  }

  // gives yyyy-mm-dd without time at the end
  today = new Date().toISOString().split('T')[0];
  $('#id_calendar').fullCalendar({
    header: {
      left: '',
      center: '',
      right: ''
    },
    defaultDate: today,
    firstDay: 1,
    defaultView: 'agendaWeek',
    eventLimit: true, // allow "more" link when too many events
    eventRender: function(event, element) {
      $(element).tooltip({title: event.title});
    },
    eventClick: function(event, jsEvent, view){
      s_idx = selected.indexOf(event.id);
      if(s_idx >= 0){
        selected.splice(s_idx);
      } else {
        selected.push(event.id);
      }
      //Update Select box with selected events
      $("#id_services").val(selected);
      $("#id_services").change();
      $(this).tooltip("destroy");
      $('#id_calendar').fullCalendar('rerenderEvents');
    },
    eventSources: [
    {
      events: services
    }]
  });

  //Update calendar with selected events
  $('#id_services').change(function() {
    selected = $("#id_services").val().map(function(t){return parseInt(t)})
    services = $('#id_calendar').fullCalendar('clientEvents');
    for (var i=0; i<services.length; i++) {
      if (selected.indexOf(services[i].id) >= 0){
        services[i].backgroundColor = "white";
      } else {
        services[i].backgroundColor = "";
      }
    }
    $('#id_calendar').fullCalendar('refetchEvents');
  });
  // call this function in the beginning to render events correctly based on selected
  $('#id_services').change();

});
