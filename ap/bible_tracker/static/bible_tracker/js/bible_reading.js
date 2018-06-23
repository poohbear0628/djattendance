
function setWeeks() {
    var firstDayofWeek = moment(first_day_term, "YYYYMMDD");
    var lastDayofWeek = firstDayofWeek.clone().add(6, 'days');
    for (i = 0; i <= current_week; i++) {
        $("#select_menu").append($("<option />").val("week-" + i).text("Week " + i + ": " + firstDayofWeek.format("ddd MMM D") + " - " + lastDayofWeek.format("ddd MMM D")).attr('id', i));
        firstDayofWeek = lastDayofWeek.add(1, 'day');
        lastDayofWeek = firstDayofWeek.clone().add(6, 'days');
    }
}

function setDatesforWeek(week) {
    enableButtons();
    var firstDay = moment(first_day_term, "YYYYMMDD");
    var firstDayofWeek = firstDay.add(week, 'weeks');
    var WedofNextWeek = firstDayofWeek.clone().add(9, 'days');
    var lastDayofWeek = firstDayofWeek.clone().add(6, 'days');
    var currentDayofWeek = firstDayofWeek.clone();
    var now = moment();
    for (var i = 0; i < 7; i++) {
        $("#day-" + i).html(currentDayofWeek.format("ddd - MMM D"));
        currentDayofWeek.add(1, 'days');
    }
    //finalize is disabled on Wednesday of next week (with HH:mm of 00:00) or before week is over (Sunday midnight+20 minutes)
    if (is_trainee && (now > WedofNextWeek || now < lastDayofWeek.clone().add(20, 'minutes'))) {
        $("#finalize").prop('disabled', true);
    }
    //save button is disabled for more than this week's Bible reading
    if (is_trainee && lastDayofWeek >= now.clone().add(6, 'days')) {
        $("#save").prop('disabled', true);
    }
}

function checkBibleReadingStatus() {
    return (bibleReading_status.match(/_/g) ? true : false);
}

function disableButtons() {
    $("#save").prop('disabled', true);
    $("#finalize").prop('disabled', true);
    $(".btn-group label").attr("disabled", true);
    $(".btn-group :input").attr("disabled", true);
    $("#bibleTrackerButton").prop('disabled', true);
    $(".bible-selector").prop('disabled', true);
}

function enableButtons() {
    $("#save").prop('disabled', false);
    $("#finalize").prop('disabled', false);
    $(".btn-group label").attr("disabled", false);
    $(".btn-group :input").attr("disabled", false);
    $("#bibleTrackerButton").prop('disabled', false);
    $(".bible-selector").prop('disabled', false);
}

function changetoFinalize() {
    // check if bible reading for the week is already finalized
    if (finalized == "Y") {
        $('#bibleTrackerButton').val("Finalize");
        disableButtons();
    }

    var timeNow = moment();
    var start = moment().day(0).hours(0).minutes(20).seconds(0);
    var end = moment().day(2).hours(23).minutes(59).seconds(59);

    // check bible reading values
    if (!checkBibleReadingStatus()) {
        // check if date is valid for user if they can finalize (from Lord's Day to Tuesday)
        if (moment(timeNow).isBetween(start, end, 'second')) {
            $('#bibleTrackerButton').val("Finalize");
        }
    }
    else {
        $('#bibleTrackerButton').val("Save");
    }
}

function modify_boxes(classname) {
    var x = document.getElementsByClassName(classname)[0];
    x.setAttribute("checked", "true");
}

function updateProgressBar(selector, data) {
    $(selector).css('width', data + '%');
    $(selector).html(data + "%");
    $(selector).attr("aria-valuenow", data);
}

/****** METHODS FOR DAILY BIBLE READING ******/
/****** METHODS FOR FIRST AND SECOND YEAR BIBLE READING ******/
function changeWeek() {
    var weekid = $("#select_menu").find('option:selected').attr('id');
    var userId = $("input#userId").val();
    var url = '/bible_tracker/?week=' + weekid
    history.pushState({ urlPath: url }, "", url)
    $('.btn.btn-primary.active').removeClass('active');

    $.ajax({
        type: "GET",
        url: change_week_url,
        dataType: 'json',
        data: {
            'week': weekid,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'userId': userId,
            'forced': forced,
        },
        success: function (data) {
            var obj = JSON.parse(data);
            var status = obj.status;
            var finalized = obj.finalized;

            setDatesforWeek(parseInt(weekid));
            var res = status.split("");
            for (i = 0; i < res.length; i++) {
                $('#status-day-' + i).find("input#" + res[i]).parent().addClass("active");
            }
            if (finalized == "Y") {
                $("#unfinalize").prop('disabled', false);
                disableButtons();
            }
            if (finalized == "N") {
                $("#save").prop('disabled', false);
                $(".btn-group label").attr("disabled", false);
                $(".btn-group :input").attr("disabled", false);
                $("#unfinalize").prop('disabled', true);
            }

            if (forced == "True") {
                $("#finalize").prop('disabled', false);
            }
        },
    });
}

function getStatus() {
    var weekly_status = ''
    for (i = 0; i < 7; i++) {
        day_status = $('#status-day-' + i + ' label.active input').val();
        if (day_status == null) {
            weekly_status += '_';
        }
        else {
            weekly_status += day_status;
        }
    }
    return weekly_status;
}

function getWeeklyStatus() {
    var code = bibleReading_status.split('');

    for (let i = 0; i < 7; i++) {
        document.getElementById("bibleDropDown_" + weekday_codes[i]).value = code[i];
    }
}

function updateStatus(finalize) {
    var weekly_status = getStatus();
    var week_id = $('#select_menu').find(":selected").attr('id');
    var userId = $("input#userId").val();
    $.ajax({
        type: "POST",
        url: update_status_url,
        data: {
            'week_id': week_id,
            'weekly_status': weekly_status,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'userId': userId,
        },
        success: function (data) {
            if (finalize) {
                finalizeStatus();
            }
            new Notification(Notification.SUCCESS, 'Saved').show();
        },
    });
}

function updateHomepageStatus(finalize) {
    var weekly_status = "";

    for (i = 0; i < 7; i++) {
        day_status = $('#bibleDropDown_' + weekday_codes[i]).val();

        // window.alert(weekday_codes[i] + " - " + day_status);
        if (day_status == " " || day_status == null) {
            weekly_status += "_";
        }
        else {
            weekly_status += day_status;
        }
    }
    bibleReading_status = weekly_status;

    $.ajax({
        type: "POST",
        url: update_status_url,
        data: {
            'week_id': current_week,
            'weekly_status': bibleReading_status,
        },
        success: function (data) {
            new Notification(Notification.SUCCESS, 'Saved').show();
        },
    });

    changetoFinalize();
}

function finalizeStatus() {
    var confirmed = confirm("Are you sure you want to finalize bible reading for this week? You will not be able to edit afterwards.");
    if (confirmed) {
        var week_id = $('#select_menu').find(":selected").attr('id');
        var userId = $("input#userId").val();
        $.ajax({
            type: "POST",
            url: finalize_status_url,
            data: {
                'week_id': week_id,
                csrfmiddlewaretoken: '{{ csrf_token }}',
                'action': 'finalize',
                'userId': userId,
                'forced': forced,
            },
            success: function (data) {
                new Notification(Notification.SUCCESS, 'Finalized').show();
                disableButtons();
                $("#unfinalize").prop('disabled', false);
            },
            error: function (data) {
                alert("Cannot finalize at this time");
            }
        });
    } else {
        //makes sure button does not stay pressed
        $("#finalize").blur();
    }
}

function finalizeFromHomePage() {
    var weekid = document.getElementById("week_select").value;
    var confirmed = confirm("Are you sure you want to finalize bible reading for this week? You will not be able to edit afterwards.");
    if (confirmed) {
        // console.log(bibleReading_status, finalized)

        $.ajax({
            type: "POST",
            url: finalize_status_url,
            data: {
                'week_id': weekid,
                'action': 'finalize',
            },
            success: function (data) {
                new Notification(Notification.SUCCESS, 'Finalized').show();
                disableButtons();
            },
            error: function (data) {
                alert("Cannot finalize at this time");
            }
        });
    } else {
        //makes sure button does not stay pressed
        $("#bibleTrackerButton").blur();
    }
}

function unfinalizeStatus() {
    var week_id = $('#select_menu').find(":selected").attr('id');
    var userId = $("input#userId").val();
    $.ajax({
        type: "POST",
        url: finalize_status_url,
        data: {
            'week_id': week_id,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'action': 'unfinalize',
            'userId': userId,
        },
        success: function (data) {
            enableButtons();
            $("#unfinalize").prop('disabled', true);
        },// success
        error: function (data) {
            alert("Sorry, there was an error processing this request."); // <- this should run if user is not activated
        } // error
    });
}

function toggleCheckbox(classname, id, year) {
    var checked = document.getElementsByClassName(classname)[0].checked;
    var userId = $("input#userId").val();
    $.ajax({
        type: "POST",
        url: update_books_url,
        data: {
            'book': id,
            'year': year,
            'checked': checked,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'userId': userId,
        },
        success: function (data) {
            let text = checked ? 'Saved' : 'Deleted';
            new Notification(Notification.SUCCESS, text).show();
            if (year == 1) {
                updateProgressBar('#first-year-prog', data);
            } else if (year == 2) {
                updateProgressBar('#second-year-prog', data);
            }
        }
    });
}

