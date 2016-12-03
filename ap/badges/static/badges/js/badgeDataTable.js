function printBadges() {
  var badge_print_list = [];
  // Assumes there's only one form in this page
  var url = $('form').attr('action');
  // get selected rows
  var inputList = table.rows('.selected').data();

  if (inputList.length <= 0) {
    alert('Please select trainees to print');
    return false;
  }

  for (var i = 0; i < inputList.length; i++) {
    badge_print_list.push(parseInt($(inputList[i][0]).attr('id')));
  }

  post(url, {
    'choice': badge_print_list,
    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
  });
}

function post(path, params) {
  var form = document.createElement("form");
  form.setAttribute("method", "post");
  form.setAttribute("action", path);

  for (var key in params) {
    if (params.hasOwnProperty(key)) {
      if (params[key].constructor === Array) {
        for (var key2 in params[key]) {
          var hiddenField = document.createElement("input");
          hiddenField.setAttribute("type", "hidden");
          hiddenField.setAttribute("name", key);
          hiddenField.setAttribute("value", params[key][key2]);

          form.appendChild(hiddenField);
        }
      } else {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
      }
    }
  }

  document.body.appendChild(form);
  form.submit();
}

var table;

function updatePrintSelectBtn() {
  // update button
  $('.print-selected').html('Print Selected (' + table.rows('.selected').data().length + ')');
}

 //custom function to generate img tags at render time (pseudo lazy loading)
 function lazyloadFnRowCallback( nRow, aData, iDisplayIndex )
 {
    $('td:eq(0)', nRow).html(aData[0].replace('data-', ''));
    return nRow;
 }

$(document).ready(function() {
  table = $('#badges-table').DataTable({
    dom: 'T<"clear">lfrtip',
    tableTools: {
      "sRowSelect": "multi",
      "aButtons": ["select_all", "select_none"]
    },
    fnRowCallback: lazyloadFnRowCallback,
    lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]]
  });

  $('.DTTT_button').on('click', function() {
    updatePrintSelectBtn();
  })

  $('#badges-table tbody').on('click', 'tr', function() {
    updatePrintSelectBtn();
  });
});
