/**
 *
 * Binds ajax api calls to buttons for lifestudy pages
 *
 */

$(window).ready(function(e) {
  // Bind click event to all delete buttons to ajax delete summaries
  $('.delete').on('click', function(ev) {
    var btn = $(this);
    // send ajax request
    $.ajax({
      url: '/api/summaries/' + btn.attr('id').split('-')[1],
      type: 'DELETE',
      success: function(response, status) {
        // remove element on page
        btn.parent().remove();
      }
    });

    return false;
  });
});
