function setWeeks(){
  var firstDayofWeek = moment(firstDayofTerm, "YYYYMMDD");
  var lastDayofWeek = firstDayofWeek.clone().add(6,'days');
  for (let i=0; i < 20; i++) {
    $("#start_range").append($("<option />").val(i).text("Week " + i + ": " + firstDayofWeek.format("ddd MMM D")).attr('id', i));
    $("#end_range").append($("<option />").val(i).text("Week " + i + ": " + lastDayofWeek.format("ddd MMM D")).attr('id', i));
    firstDayofWeek = lastDayofWeek.add(1,'day');
    lastDayofWeek = firstDayofWeek.clone().add(6,'days');
  }
}

$( document ).ready(function() {
    $("#extra_options").hide();

    $('#results').DataTable({
      paging: false,
      columnDefs: [
        {
          targets: 'no-sort',
          orderable: false,
        },
        {
          targets: options,
          visible: true
        },
        {
          targets: 'trainee-info',
          visible: true
        },
        {
          targets: '_all',
          visible: false
        }
      ],
      dom: '<"row"<"col-sm-6"Bl><"col-sm-6"f>>' +
        '<"row"<"col-sm-12"<"table-responsive"tr>>>' +
        '<"row"<"col-sm-5"i><"col-sm-7"p>>',
      fixedHeader: {
        header: true
      },
      buttons: {
        buttons: [
          {
            extend: 'print',
            text: 'Print',
            filename: 'Bible Reading Report',
            title: 'Bible Reading Report',
            autoPrint: true,
            exportOptions:{
              columns: ':visible'
            },
          },
          {
            extend: 'csvHtml5',
            text: 'CSV',
            filename: 'Bible Reading Report',
            title: 'Bible Reading Report',
            exportOptions: {
              columns: ':visible'
            },
          },
          {
            extend: 'pdf',
            text: 'PDF',
            filename: 'Bible Reading Report',
            title: 'Bible Reading Report',
            exportOptions:{
              columns: ':visible'
            },
          },
          {
            extend: 'colvis',
            text: 'Show/Hide Columns',
            columns: ':gt(1)',
          },
        ],
        dom: {
          container: {
            className: 'dt-buttons'
          },
          button: {
            className: 'btn btn-default'
          }
        }
      }
    });

    setWeeks();

    $('.more_or_less').click(function() {
      $('#more').toggle("display");
      $("#extra_options").toggle();
    });

    for (i=0; i < options.length; i++){
      $('#bible_reading_report input[value=' + options[i] + ']').prop('checked', true);
    }
})
