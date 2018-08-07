var pageVersion;
var oldAns = [];
var checkAnns = false;
function displayTicker(ans) {
  $("#ticker").html("");

  //Reloads when the announcements change
  if (checkAnns) {
    if (oldAns.length !== ans.length) {
      location.reload(true);
    }
    ans = ans.concat().sort();
    oldAns = oldAns.concat().sort();
    for(var i = 0; i < ans.length; i++) {
      if (ans[i] !== oldAns[i]) {
        location.reload(true);
      }
    }
  }
  else {
    oldAns = ans;
    checkAnns = true;
  }
  var anslen = ans.length;
  var temp = $("<span></span>");
  for (var i = 0; i < anslen; i++) {
    //Format ticker announcements here
    temp.append("<b>&ltAnnouncement #" + (i+1) + ":</b> " + ans[i] + "<b>&gt</b>&nbsp&nbsp");
  }
  var anns = $("<p style=\"white-space:nowrap\"></p>");
  $("#ticker").append(anns.append(temp));
  var anns_size = $("#ticker").width();

  var total_size = anns_size + $(document).width();
  $("#ticker").animate({left: "100%"},0,"linear");
  $("#ticker").animate({left: "-" + anns_size + "px"},total_size*10,"linear");
}

function loadTicker() {
  $.getJSON(TICKER,displayTicker)
  .fail(function() {
    displayTicker(oldAns);
  });
}

var OFFSETS = [
  {offset: 0, limit: 11, oldRooms: []},
  {offset: 11, limit: 11, oldRooms: []},
  {offset: 22, limit: 11, oldRooms: []},
];

function displayRooms(rooms) {
  $("#schedule").html("");
  var currentTime = new Date(new Date().getTime() - 30*60000); //minus 30 min because first row doesn't have time
  var hour = currentTime.getHours();
  var minute = Math.floor(currentTime.getMinutes() / 30) * 30;
  currentTime = new Date(currentTime.toLocaleDateString("en-US") + " " + hour + ":" + minute);
  var NUM_ROWS = 7;
  var NUM_COLS = rooms.length + 1;
  for (var rowNum = 0; rowNum < NUM_ROWS; rowNum++) {
    var row = $("<tr></tr>");
    for (var colNum = 0; colNum < NUM_COLS; colNum++) {
      var cell = $("<td></td>", {"class": "cell"});
      if (rowNum === 0) {
        cell.attr("class", "top-row");
        if (colNum === 0) {
          cell.text("TIME");
        } else {
          cell.text(rooms[colNum - 1].name);
        }
      } else if (colNum === 0) {
        cell.text(formatAMPM(currentTime));
      } else {
        var res = rooms[colNum - 1].res;
        $.each(res, function(i, info) {
          hour = currentTime.getHours();
          minute = Math.floor(currentTime.getMinutes() / 30) * 30;
          if (info.time === (("0" + hour).slice(-2) + ":" + (minute ? "30" : "00"))) {
            cell.attr("class", "cell occupied");
            cell.html("<span>" + info.content + "</span>");
          }
        });
      }
      row.append(cell);
    }
    currentTime = new Date(currentTime.getTime() + 30*60000);
    $("#schedule").append(row);
  }
}

function loadCalendar() {
  var currentOffset = OFFSETS.shift();
  $.getJSON(RESERVATIONS + "?offset=" + currentOffset.offset + "&limit=" + currentOffset.limit,
    (rooms) => {
      currentOffset.oldRooms = rooms;
      displayRooms(rooms);
      OFFSETS.push(currentOffset);
    }
  )
  .fail(() => {
    displayRooms(currentOffset.oldRooms);
    OFFSETS.push(currentOffset);
  });
}

function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  hours = hours ? hours : 12;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  var strTime = hours + ":" + minutes + " " + ampm;
  return strTime;
}

var oldWeather;
function loadWeather() {
  $.getJSON(WEATHER_API, updateWeather)
  .fail(function() {
    updateWeather(oldWeather);
  });
}
function updateWeather(weather) {
  oldWeather = weather;
  var condition = weather.query.results.channel.item.condition;
  var forecasts = weather.query.results.channel.item.forecast;
  $("#today-temp").html(condition.temp + "&deg;");
  var conditions = [$("#today-condition"), $("#tomorrow-condition"), $("#daft-condition")];
  var lows = [$("#today-low"), $("#tomorrow-low"), $("#daft-low")];
  var highs = [$("#today-high"), $("#tomorrow-high"), $("#daft-high")];
  for (var i = 0; i < 3; i++) {
    var forecast = forecasts[i];
    lows[i].html("L " + forecast.low + "&deg;");
    highs[i].html("H " + forecast.high + "&deg;");
    conditions[i].attr("class", "wi wi-" + WEATHER_CODES[forecast.code]);
  }
  $("#daft").text(forecasts[2].day);
}

function updateClock()
{
  var currentTime = new Date();
  var currentSeconds = currentTime.getSeconds();
  currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;
  var minutesAndHours = formatAMPM(currentTime).split(" ");
  var timeOfDay = minutesAndHours[1];
  var currentTimeString = minutesAndHours[0]  + ":" + currentSeconds;
  var hour = currentTimeString.split(":")[0];
  if (hour.length < 2) {
    currentTimeString = " " + currentTimeString;
  }
  $("#clock").text(currentTimeString);
  $("#ampm").text(timeOfDay);
  var options = {
    weekday: "long", year: "numeric", month: "long",
    day: "numeric"
  };
  $("#date").html(currentTime.toLocaleDateString("en-us", options));

  setTimeout(updateClock, 1000 - (currentTime.getTime() % 1000))
}

$(document).ready(function() {
  loadCalendar();
  setInterval(loadCalendar, 10000);
  loadWeather();
  setInterval(loadWeather, 10000);
  updateClock();
  loadTicker();
  setInterval(loadTicker, 1000); //Checks for changes in the announcements

  setInterval(function() {
    $.get(PAGE_VERSION + "?random=" + Math.random(), function(data) {
      if (pageVersion !== data) {
        location.reload(true);
      }
    });
  }, 60*1000);
  $.get(PAGE_VERSION, function(data) {
    pageVersion = data;
  });
});
