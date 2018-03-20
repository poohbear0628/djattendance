$(document).ready(() => {

  // to change weekday codes into dates of the month
  day_end.setDate(day_end.getDate() + 6);
  var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  var cws = monthNames[day_start.getMonth()] + " " + day_start.getDate() + " - " + monthNames[day_end.getMonth()] + " " + day_end.getDate() + ", " + day_end.getFullYear();
  $(".cws").html(cws);

  var note_date = new Date(day_start);
  note_date.setDate(note_date.getDate() + 4);
  $(".notice_date").html(monthNames[note_date.getMonth()] +  " " + note_date.getDate());

  var datebox = "<td>" + day_start.getDate() + "</td>";

  for (i=1; i < 7; i++){

    var datebox_Date = new Date(day_start);
    datebox_Date.setDate(datebox_Date.getDate() + i);
    datebox = datebox + "<td>" + datebox_Date.getDate() +"</td>";
  };

  $(".this_week").html(datebox);


});
