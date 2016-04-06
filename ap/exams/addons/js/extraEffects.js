/* 
 * Extra effects for jQuery
 * Author: Allen Webb
 */
(function($){
    var loop = function(item,delay,callback){
        delay = Math.ceil(delay);
        var step = function(){
            callback();
            item.step_timer = setTimeout(step,delay);
        };
        item.step_timer = setTimeout(step,delay);
    }
    var animate = function(item,delay,fps,each,end){
        var parts = Math.ceil(delay/1000*fps);
        var inc=0;
        loop(item,delay/parts,function(){
            if(inc++==parts){
                end();
                inc=0;
            } else each(parts,inc);
        });
    }
    $.fn.verticalScroll = function(delay,fps){
        this.each(function(){
            var parent = $(this);
            animate(parent,delay,fps,function(parts,inc){
                var child = parent.children(":first");
                var child2 = parent.children(":nth-child(2)");
                if(child.length==0||child2.length==0) return;
                var height = child2.offset().top-child.offset().top;
                parent.scrollTop(height/parts*inc);
            },function(){
                var child = parent.children(":first");
                child.hide().remove().appendTo(parent).fadeIn('fast');
                parent.scrollTop(0);
            });
        });
    };
    $.fn.horizontalScroll = function(delay,fps){
        this.each(function(){
            var parent = $(this);
            animate(parent,delay,fps,function(parts,inc){
                var child = parent.children(":first");
                var child2 = parent.children(":nth-child(2)");
                if(child.length==0||child2.length==0) return;
                var height = child2.offset().left-child.offset().left;
                parent.scrollLeft(height/parts*inc);
            },function(){
                var child = parent.children(":first");
                child.hide().remove().appendTo(parent).fadeIn('fast');
                parent.scrollLeft(0);
            });
        });
    };
    $.fn.fadeThrough = function(delay){
        delay=Math.max(1200,delay);
        this.each(function(){
            var parent = $(this);
            var child = parent.children(":first");
            parent.children().not(child).hide();
            loop(parent,delay,function(){
                if(parent.children().length<2)
                    return;
                var next = child.next();
                if(next.length==0) next = parent.children(":first");
                child.fadeOut('slow',function(){
                    next.fadeIn('slow',function(){
                    child=next; 
                    });
                });
            });
        });
    };
    $.fn.stopExtraEffect = function(){
        this.each(function(){
            if(this.step_timer)
                clearTimer(this.step_timer);
            this.step_timer=null;
        });
    };
})($);
