/* 
 * Generic ajax functionality
 * 
 * To make this work with an input, set the table attribute of the input and give it the post_on_change class.
 * 
 * author: Allen Webb
 */

$(document).ready(function(){
    var savedTimeout;
    var notice = $('<div id="saved_notice" style="position: absolute; font-size: 16px; background-color: white; border-radius: 3px 3px 3px 3px; color: #0A0; display: none;">Saved!</div>').appendTo('#Content');
    function handler(select,data){
        $.ajax({
            'url':'?ajax='+select.attr('table'),
            'data':data,
            'success':function(data){
                if(data){
                    console.log(data);
                    //probably logged out
                    select.each(function(){
                        var select_ = $(this);
                        select_.val(select_.attr('oldValue'))
                    });
                    window.open('./');
                } else {
                    select.each(function(){
                        var select_ = $(this);
                        select_.attr('oldValue',select_.val());
                    });
                    var offset = select.offset();
                    notice.css({'top':offset.top+'px','left':offset.left+'px'}).fadeIn();
                    if(savedTimeout) clearTimeout(savedTimeout);
                    savedTimeout = setTimeout(function(){
                        notice.fadeOut();
                        savedTimeout=null;
                    },1500);
                }
            },
            'error':function(){
                select.each(function(){
                    var select_ = $(this);
                    select_.val(select_.attr('oldValue'))
                });
                alert('Unable to submit. Please check your connection.');
            }
        });
    }
    
    $('.post_on_change:input').change(function(){
        var select = $(this);
        handler(select,select.serialize());
    }).each(function(){
        var this_=$(this);
        this_.attr('oldValue',this_.val());
    });
    
    $('.post_on_change :input').change(function(){
        var select = $(this).parents('.post_on_change:first').find(':input');
        handler(select,select.serialize());
    }).each(function(){
        var this_=$(this);
        this_.attr('oldValue',this_.val());
    });
    
});