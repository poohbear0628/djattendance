var SmartTable = {
  //Variables
  headers: {},
  content: [],
  options: {
    table_id: "",
    add_row_id: "",
    delete_row: function(e, elem){
      console.log(e);
    },
    add_row: function(e, elem){
      console.log(e);

    },
    content_change: function(e, elem){
      console.log(e);
    }
  },

  init: function(opts, header, content){
    var t = SmartTable;
    for (var k in opts){
      if(t.options[k] != null){
        t.options[k] = opts[k];
      }
    }

    t.headers = header;
    t.content = content;

    //Draw the table on init
    t.draw_table();
    t.add_listeners();

    return t;
  },

  draw_table: function(){
    var t = SmartTable;
    var c = "";

    //Build header row
    c += "<thead><tr>";
    for(k in t.headers){
      c += "<th>"+t.headers[k]+"</th>";
    }
    c += "</tr></thead>";
    c += "<tbody>";
    //Add content rows
    for(var i=0; i<t.content.length; i++){
      var row = t.content[i];
      c += "<tr>";
      for(var k in t.headers){
        c += "<td";
        if(k == "delete"){
          c += "><button type='button' class='btn btn-danger section_delete' data-row='"+i+"' data-col='"+k+"'><span class='glyphicon glyphicon-remove'></span></button>";
        } else {
          c += " contenteditable class='sectionInputs' data-row='"+i+"' data-col='"+k+"'>"+row[k];
        }
        c += "</td>";
      }
      c += "</tr>";
    }
    c += "</tbody>";
    console.log(c);
    $("#"+t.options.table_id).html(c);
  },

  add_listeners: function(){
    var t = SmartTable;

    $('body').on('blur', '.sectionInputs', function(e) {
      //Content edit
      var button = $(e.currentTarget);
      var row = button.data('row');
      var col = button.data('col');
      t.content[row][col] = button.text();
      t.options.content_change(e, e.currentTarget);
    }).on('click', '.section_delete', function(e){
      //Delete button
      var button = $(e.currentTarget);
      var row = button.data('row');
      var col = button.data('col');
      var deleted = t.content.splice(row, 1);
      t.draw_table();
      t.options.delete_row(e, e.currentTarget, deleted);
    });
    //Add row button
    $("#"+t.options.add_row_id).click(function(e){
      // Do a check if last row has anything filled. If all columns are empty then don't add a new row
      if(t.content.length > 0){
        var obj = t.content[t.content.length-1];
        for(var keys = Object.keys(obj), i = 0, end = keys.length; i < end; i++) {
          if (obj[keys[i]] != ""){
            break;
          }
          if((i+1) == end){
            return;
          }
        }
      }
      var row = {};
      for(var k in t.headers){
        row[k] = "";
      }
      t.content.push(row);
      t.draw_table();
      t.options.add_row(e, e.currentTarget);
    });
  }

};