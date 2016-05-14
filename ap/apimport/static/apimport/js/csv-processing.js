function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function post_locality(id){
    var city_name = $('#id_form-' + id + '-name').val();
    var state_id = $('#id_form-' + id + '-state').val();
    var country_code = $('#id_form-' + id + '-country').val();

    console.log("posting");
    $.ajax({
        type:"POST",
        url: "save-data",
        data: {
            'type' : 'locality',
            'city_name' : city_name,
            'state_id' : state_id,
            'country_code' : country_code,
            csrfmiddlewaretoken: getCookie('csrftoken')
        },
        success: function(data){
            console.log("success message received");
            console.log(id + " test");
            $('#locality_' + id).hide(400);
        }
    });

    return false;   
}