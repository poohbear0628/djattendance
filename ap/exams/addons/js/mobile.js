$(document).ready(function(){
    var line=450;
    var past_width=800;
    var nav = $('#Nav');
    var main = $('#Main');
    if(nav.length==1 && main.length==1){
        $(window).resize(function(event){
            var width = $(this).width();
            if(width <= line && past_width > line) {
                nav.css({'float':'none'});
                main.css({'margin':'5px'});
            } else if (width > line && past_width <= line) {
                nav.css({'float':'left'});
                main.css({'margin':'0px 30px 0px 180px'});
            }
            past_width=width;
        }).resize();
    } else if(main.length==1){
        $(window).resize(function(event){
            var width = $(this).width();
            if(width <= line && past_width > line) {
                main.css({'margin':'5px'});
            } else if (width > line && past_width <= line) {
                main.css({'margin':'0px 30px 0px 30px'});
            }
            past_width=width;
        }).resize();
    }
});