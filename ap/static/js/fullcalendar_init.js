$(document).ready(function() {
  var color_list = [];
  var base_color = xolor('darkslateblue');

  for (var i=0; i<NUM_OF_COLORS+1; i++) {
    var color = base_color.gradient('yellowgreen', i / NUM_OF_COLORS).hex;
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

  var today = moment().format('YYYY-MM-DD');
  $('#id_calendar').fullCalendar({
    header: {
      left: 'listWeek, agendaWeek, agendaDay',
      center: '',
      right: 'prev, next'
    },
    minTime: "05:00:00",
    maxTime: "23:00:00",
    defaultDate: today,
    firstDay: 1,
    defaultView: 'agendaWeek',
    views: {
      agendaDay:{
        type: 'agenda',
        duration: {days: 1}
      }
    },
    eventLimit: true, // allow "more" link when too many events
    eventRender: function(event, element) {
      $(element).tooltip({title: event.title});
    },
    eventClick: function(event, jsEvent, view){
      s_idx = selected.indexOf(event.id);
      if(s_idx >= 0){
        selected.splice(s_idx, 1);
      } else {
        selected.push(event.id);
      }
      //Update Select box with selected events
      $(this).tooltip("destroy");
      $("#id_services").val(selected);
      $("#id_services").change();
      // $('#id_calendar').fullCalendar('rerenderEvents');
    },
    eventSources: [
    {
      events: services
    }]
  });

  //Update calendar with selected events
  $('#id_services').change(function() {
    if($("#id_services").val()){
      selected = $("#id_services").val().map(function(t){return parseInt(t)})
    } else {
      selected = Array();
    }
    console.log(selected);
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
