$(document).ready(function(){
  var base_url = window.location.protocol + '//' + window.location.host;
  var api_base = '/api'

  function getEvents(data) {
    console.log('>>>>???')
    var event_groups = {'code': [],
                'type': [],
                'class_type': [],
                'start': [],
                'end': [],
                'day': [],
                'weekday': [],
                'schedules': [],
               }

    var deferreds = []; // all ajax deferred objects get pushed into here
    
    if (data['code']) {
      console.log(data['code'])
      console.log(base_url + api_base + '/allevents?code=' + data['code'].val() + '/?format=json')
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?code=' + data['code'].val() + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            console.log(data)
            event_groups['code'] = getEventIDs(data);
          }
        }));
    }

    for (i = 0; i < data['type'].length; i++) {
      console.log(data['type'])
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?type=' + data['type'][i] + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['type'] = [...new Set([...event_groups['type'], ...getEventIDs(data)])];
          }
        }));
    }

    for (i = 0; i < data['class_type'].length; i++) {
      console.log(data['class_type'])
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?class_type=' + data['class_type'][i] + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['class_type'] = [...new Set([...event_groups['class_type'], ...getEventIDs(data)])];
          }
        }));
    }

    if (data['start']) {
      console.log(data['start'])
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?start=' + data['start'] + '?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['start'] = getEventIDs(data);
          }
        }));
    }

    if (data['end']) {
      console.log(data['end'])
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?end=' + data['end'] + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['end'] = getEventIDs(data);
          }
        }));
    }

    if (data['day']) {
      console.log(data['day'])
      deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?day=' + data['day'] + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['day'] = getEventIDs(data);
          }
        }));
    }
    
    if (data['weekday']) {
        console.log(data['weekday'])
        deferreds.push(
        $.ajax({
          url: base_url + api_base + '/allevents?weekday=' + data['weekday'] + '/?format=json',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          success: function(data) {
            event_groups['weekday'] = getEventIDs(data);
          }
        }));
    }

    if (data['schedules']!==null) {
      console.log(data['schedules'])
      for (i = 0; i < data['schedules'].length; i++) {
        if(data['schedules'][i] === "") continue;
        deferreds.push(
          $.ajax({
            url: base_url + api_base + '/events?schedules=' + data['schedules'][i].id + '/?format=json',
            contentType: 'application/json',
            data: data,
            dataType: 'json',
            success: function(data) {
              event_groups['schedules'] = [...new Set([...event_groups['schedules'], ...getEventIDs(data)])];
            }
          }));
      }
    }

    // when all ajax calls are successful, find intersection of
    // all event groups and add events to event field.
    $.when.apply($, deferreds).then(function(){
      console.log('??qweqwe21rg')
      var intersect = [];
      for (k in data) {
        if (data[k] != false && data[k] != undefined) {
          intersect.push(event_groups[k])
        }
      }
      console.log(intersect)
      if (intersect.length!==0) {
        addEvents(intersect.reduce((arr1,arr2) => arr1.filter(x => new Set(arr2).has(x))));
      }
    });
  }

  // data: events in JSON
  // return array of event ids
  function getEventIDs(data) {
    var event_ids = [];
    for (i = 0; i < data.length; i++) {
      event_ids[event_ids.length] = data[i]['id'];
    };
    return event_ids;
  }

  // data: array of event ids to be added into the event field
  // function selects events in event Select2 field.
  function addEvents(event_ids) {
    console.log(event_ids)
    var curr = ($('#id_events').val())
    if (curr[0]!=='') {
      event_ids = [...new Set([...curr, ...event_ids])]
    }
    $('#id_events').val(event_ids).trigger('change');
    return;
  }
  $('#add_events').click(function(event) {
    event.preventDefault();
    form_data = {
      'code': $("#id_code"),
      'type': getValues($('input[name=type]:checked')),
      'class_type': getValues($('input[name=class_type]:checked')),
      'start': $("#id_start"),
      'end': $("#id_end"),
      'day': $("#id_day"),
      'weekday': getValues($('input[name=weekday]:checked')),
      'schedules': $("#id_schedule").val(),
    };
    getEvents(form_data);
    clearForm();
    $('#event_select').modal('hide');
  })

  function getValues(object) {
    var values = [];
    object.each(function() {
      values[values.length] = $(this).attr('value');
    })
    return values;
  }

  function clearForm() {
    $('#event_select')[0].reset();
    $('#id_schedule').select2().val(null).trigger('change');
  }
})
