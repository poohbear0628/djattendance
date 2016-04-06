/** Javascript for drawing lines between divs on the database structure visualization page
 * @author Allen Webb
 */
var links;
var same;
var colors;
var timer_itr_loc;
var ignore_flag;

function itr_loc_loop(){
    iterateLocations();
    timer_itr_loc = setTimeout(itr_loc_loop,20);
}

$(document).ready(function(){
    links = {};
    same = {};
    colors = {count: 0};

    $('#itr_loc').bind({
        dblclick: function(){
            ignore_flag=1;
            itr_loc_loop();
        },
        mousedown: function(){
            if(timer_itr_loc)
                clearTimeout(timer_itr_loc);
            else
                itr_loc_loop();
        },
        mouseup: function(){
            if(ignore_flag){
                ignore_flag--;
                return;
            }
            if(timer_itr_loc)
                clearTimeout(timer_itr_loc);
            timer_itr_loc=null;
        }
    });
    $('#space div').dblclick(function(){$(this).toggleClass('locked');});
    var x, y;
    var list = $('#space div').bind('drag',function(){drawVisible();});
    var off_list = new Array();
    for(x=0; x<list.length; x++){
        $(list[x]).attr('processed',1);
        for(y=0; y<list.length; y++){
            if(x==y)
                continue;
            findMatches(list[x],list[y]);
        }
        off_list.push($(list[x]).position());
    }
    for(x=0; x<list.length; x++){
        var off=off_list.shift();
        console.log(off.top+","+off.left);
        $(list[x]).css({position:'absolute'}).css({top:Math.round(off.top)+'px',left:Math.round(off.left)+'px'});
    }
    delete off;

    $(window).scroll(function(){drawVisible();});
    findColors();
    drawVisible();
});

function findColors(){
    var count = colors.count;
    var x=0, dx=1.0/count;
    var string = "<style type='text/css'>\n";
    for(var prop in colors){
        if(prop=='count')
            continue;
        colors[prop]='hsl('+Math.round(x*360)+',100%,50%)';
        string+="."+prop+"{color:hsl("+Math.round(x*360)+",100%,20%);}\n";
        x+=dx;
    }
    $(string+"</style>").appendTo("head");
}

function findMatches(divA,divB){
    var a=0;
    var b=0;

    var idA=divA.id;
    var idB=divB.id;
    var listItemsA = $(divA).find('li');
    var listItemsB = $(divB).find('li');

    var procB = $(divB).attr('processed');

    for(a=0; a<listItemsA.length; a++){
        var check=idA+listItemsA[a].innerHTML;
        var skipFlag=false;
        switch(listItemsA[a].innerHTML.toLowerCase())
        {
            case 'active':
            case 'code':
            case 'comments':
            case 'description':
            case 'id':
            case 'name':
            case 'notes':
            case 'remarks':
            case 'timestamp':
                skipFlag=false;
                break;
            default:
                skipFlag=true;
                break;
        }
        for(b=0; b<listItemsB.length; b++){
            if(listItemsB[b].innerHTML.toLowerCase().indexOf(check.toLowerCase())!=-1){
                if(! colors[check.toLowerCase()]){
                    colors[check.toLowerCase()]=true;
                    colors.count++;
                }
                if(!links) {links={};}
                if(!links[idA]) links[idA]={};
                if(!links[idB]) links[idB]={};
                if(!links[idA][idB]) links[idA][idB] = new Array();
                if(!links[idB][idA]) links[idB][idA] = new Array();
                links[idA][idB].push(check);
                links[idB][idA].push(check);
                if(!$(listItemsA[a]).hasClass(check.toLowerCase()))
                    $(listItemsA[a]).addClass(check.toLowerCase());
                if(!$(listItemsB[b]).hasClass(check.toLowerCase()))
                    $(listItemsB[b]).addClass(check.toLowerCase());
            }
            if(! procB && skipFlag && listItemsB[b].innerHTML.toLowerCase()==listItemsA[a].innerHTML.toLowerCase()){
                if(!same) same={};
                if(!same[idA]) same[idA]={};
                if(!same[idB]) same[idB]={};
                if(!same[idA][idB]) same[idA][idB] = new Array();
                if(!same[idB][idA]) same[idB][idA] = new Array();
                same[idA][idB].push(listItemsA[a]);
                same[idB][idA].push(listItemsA[a]);
            }
        }
    }
}

function calcDist(locA,locB){
    var distX = locA.x-locB.x;
    var distY = locA.y-locB.y;
    var r = Math.sqrt(distX*distX+distY*distY);
    if(r!=0){
        distX/=r;
        distY/=r;
    }
    return {r: r, dy: distY, dx: distX};
}

function iterateLocations(){
    var rep_str = .25;
    var rep_dist = 250;
    var atr_dist = 350;
    var atr_str = .025;
    var list = $('#space div');
    var a;
    var b;
    var positions = new Array();
    for(a=0; a<list.length; a++){
        var off = $(list[a]).position();
        var x=off.left+$(list[a]).width()/2;
        var y=off.top+$(list[a]).height()/2;
        positions.push({x:x,y:y,top:off.top,left:off.left});
    }
    for(a=0; a<list.length; a++){
        if($(list[a]).hasClass('locked'))
            continue;
        var locA = positions[a];
        var netx=0;
        var nety=0;
        for(b=0; b<list.length; b++){
            if(a==b)
                continue;
            var locB = positions[b];
            var dist = calcDist(locA,locB);
            if(dist.r<rep_dist){
                var rep = (rep_dist - dist.r)*rep_str;
                netx+=rep*dist.dx;
                nety+=rep*dist.dy;
            }
            if(links[list[a].id] && links[list[a].id][list[b].id] && dist.r>atr_dist){
                var atr = (dist.r-atr_dist)*atr_str;
                netx-=atr*dist.dx;
                nety-=atr*dist.dy;
            }
        }
        var top = Math.max(positions[a].top+nety,0);
        var left = Math.max(positions[a].left+netx,0);
        $(list[a]).css('top',top+'px').css('left',left+'px');
    }
    delete positions;
    drawVisible();
}

function drawVisible(){
    var top = $(document).scrollTop();
    var left = $(document).scrollLeft();
    var height = $(window).height();
    var width = $(window).width();
    var bottom = top+height;
    var right = left+width;

    var visible = {};

    var result = $('#lines');
    if(result.length!=1 || !result[0].getContext)
        return false;
    result[0].width=width;
    result[0].height=height;
    var context = result[0].getContext('2d');
    context.clearRect(0, 0, result[0].width, result[0].height);
    context.lineWidth = 2;

    $('#space div').each(function(){
        var off = $(this).offset();
        var x1=off.left, x2=x1+$(this).width();
        var y1=off.top, y2=y1+$(this).height();
        //console.log(y1+","+y2+","+x1+","+x2);
        //if(((top<=y1 && y1<bottom)||(top<y2 && y2<=bottom))&&((left<=x1 && x1<right)||(left<x2 && x2<=right))){
            var id = $(this)[0].id;
            visible[id]={x:(x1+x2)/2,y:(y1+y2)/2};
        //}
    });
    for(var idA in visible){
        if(links[idA]) for(var idB in links[idA]){
            if(visible[idB]){
                context.beginPath()
                context.strokeStyle = colors[links[idA][idB][0].toLowerCase()];
                var pnt1 = visible[idA];
                var pnt2 = visible[idB];
                context.moveTo(pnt1.x-left,pnt1.y-top);
                context.lineTo(pnt2.x-left,pnt2.y-top);
                context.stroke();
            }
        }
    }
}

