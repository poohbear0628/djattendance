/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */
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
  // attach fastclick to remove click delay on mobile
  fastclick.attach(document.body);
  // Makes all textarea elastic (resize according to content)
  autosize($('textarea'));
  // Initialize the code that does the navbar stuff
  $('[data-toggle="offcanvas"]').click(function () {
    $('.row-offcanvas').toggleClass('active')
  });

  let jqXhr = $.ajaxSettings.xhr
  let $ajaxHR = $('#ajaxStatus')
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    },
    xhr: function(){
      let xhr = jqXhr()
      xhr.upload.onprogress = evt => {
        $ajaxHR.show()
        if (evt.lengthComputable) {
          $ajaxHR.animate({'width': evt.loaded/evt.total * 100 + '%'}, 'slow')
        } else {
          $ajaxHR.animate({'width': '50%'}, 'slow')
        }
      }
      xhr.upload.onloadend = () => {
        $ajaxHR.animate({'width': '100%'}, 'slow', null, () => {
          $ajaxHR.fadeOut()
          $ajaxHR.css({'width': '0'})
        })
      }
      return xhr ;
    }
  });

  updateClock();
  setInterval(updateClock, 1000);
});

function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12;
  hours = hours ? hours : 12;
  minutes = minutes < 10 ? '0' + minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}

function updateClock() {
  var currentTime = ServerDate;
  var currentSeconds = currentTime.getSeconds();
  var offset = currentTime.getPrecision();
  currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;
  var minutesAndHours = formatAMPM(currentTime).split(' ');
  var timeOfDay = minutesAndHours[1];
  var currentTimeString = minutesAndHours[0]  + ":" + currentSeconds;
  var hour = currentTimeString.split(':')[0];
  if (hour.length < 2) {
    currentTimeString = ' ' + currentTimeString;
  }
  $("#clock").text(currentTimeString);
  $("#ampm").text(timeOfDay);
  $("#offset").text("± " + offset + "ms");
  var options = {
    weekday: "long", year: "numeric", month: "long",
    day: "numeric"
  };
  $("#date").html(currentTime.toLocaleDateString('en-us', options));
}
