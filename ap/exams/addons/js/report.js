function saveReport(btn) {
    var throbber = new Throbber("Saving...", null, false);
    var saveDiv = dojo.byId("saveDiv");
    throbber.lockButton(btn);
    throbber.append(btn);
    throbber.insertAfter(saveDiv);
    
    var reportname = dojo.byId("reportName").value;
    
    var bindArgs = {
        url: "processSaveReport.php",
        content: {reportname: reportname, columns: columns},
        load: dojo.lang.hitch(this, function(type, data) {
            dojo.byId("msgDiv").value = data;
            //alert(data);
        })
    };
    
    dojo.io.bind(bindArgs);
    throbber.done();
}
