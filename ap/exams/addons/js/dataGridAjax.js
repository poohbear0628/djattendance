/** 
 * dataGridAjax.js
 * This was written to add ajax functionality to pages that use the data-grid
 * format for roll entry
 * 
 * @author Allen Webb
 */

$(document).ready(function(){
    $("tr#set_all").remove(); //this can be removed once the set_all column is fixed to work with the ajax
    $("#rollGrid input.cell").change(function(){
        var data = {};
        var new_name=$(this).prop("name");
        var new_value=$(this).val();
        var old_name=$(this).next("input").prop("name");
        var old_value=$(this).next("input").val();
        data[new_name]=new_value;
        data[old_name]=old_value;
        $.ajax({type: "POST", url: "proc.roll.php?ajax=1",
                'data': data,
                'success': function(msg){
                    $('input[name="'+old_name+'"]').val(new_value);
                    var saved1 = $("<div style='position: absolute; margin:0px; padding: 2px; font-weight: bold; color: #3E3; background-color: #FFF; font-size: 14px;'>Saved!</div>");
                    var saved2 = $("<div style='position: absolute; margin:0px; padding: 2px; font-weight: bold; color: #3E3; background-color: #FFF; font-size: 14px;'>Saved!</div>");
                    $("#rollGrid thead th:first").prepend(saved1).before(msg);
                    $("table.traineeTable").not("#rollGrid").find("thead th:first").prepend(saved2);
                    setTimeout(function(){
                        saved1.fadeOut('slow',function(){
                            saved1.remove();
                        });
                        saved2.fadeOut('slow',function(){
                            saved2.remove();
                        });
                    },500);
                },
                'error': function(){
                    alert("Error: Check your network connection!");
                    $('input[name="'+new_name+'"]').val(old_value);
                }
            });
    });
});