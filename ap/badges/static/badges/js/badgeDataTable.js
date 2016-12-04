function printBadges() {
  var badge_print_list = [];
  // Assumes there's only one form in this page
  var url = $('form').attr('action');
  // get selected rows
  var inputList = table.rows('.selected').data();
  var copies = 1;

  if (inputList.length <= 0) {
    alert('Please select trainees to print');
    return false;
  }

  for (var i = 0; i < inputList.length; i++) {
    badge_print_list.push(parseInt($(inputList[i][0]).attr('id')));
  }

  if(badge_print_list.length < 8){
    // Try to guestimate best number based on selected number
    copies = parseInt(8/badge_print_list.length);
    console.log(badge_print_list.length);
    copies = prompt("Enter number of duplicates for each person selected", copies);
  }

  post(url, {
    'choice': badge_print_list,
    'copies': copies,
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
  $('#badges-table tfoot th').each( function () {
      var title = $(this).text();
      if (title != ""){
        $(this).html( '<input type="text" />' );
      }
    });

  table = $('#badges-table').DataTable({
    dom: 'T<"clear">lfrtip',
    tableTools: {
      "sRowSelect": "multi",
      "aButtons": [{
          "sExtends": "select_all",
          "sButtonText": "Select All",
          "fnClick": function (nButton, oConfig, oFlash) {
            var oTT = TableTools.fnGetInstance('badges-table');
            oTT.fnSelectAll(true); //True = Select only filtered rows (true). Optional - default false.
          }
        }, "select_none"]
    },
    fnRowCallback: lazyloadFnRowCallback,
    lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]]
  });

  // Apply the search
  table.columns().every( function () {
      var that = this;

      $( 'input', this.footer() ).on( 'keyup change', function () {
          if ( that.search() !== this.value ) {
              that
                  .search( this.value )
                  .draw();
          }
      });
  });

  $('.DTTT_button').on('click', function() {
    updatePrintSelectBtn();
  })

  $('#badges-table tbody').on('click', 'tr', function() {
    updatePrintSelectBtn();
  });
});
