
var color = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"];
var st_ns = [[0], [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12], [13]];
var ns = [];
var n_tot = 14;
var scaling = 40;
var X_OFFSET = 200;
var MARGIN = 100;
var max_stage_length = 7;

// source/sink
//ns.push({id: 0, fixed: true, x: 100, y: services * scaling});
//ns.push({id: n_tot - 1, fixed: true, x: 500, y: services * scaling});

for (var i in st_ns) {
  // In stage i nodes
  var ns_i = st_ns[i];
  var Y_OFFSET = (max_stage_length - ns_i.length) / 2;
  for (var j in ns_i) {
    var n = ns_i[j];
    ns.push({id: n, fixed: true, x: MARGIN + i * X_OFFSET, y: MARGIN + (Y_OFFSET + parseInt(j)) * scaling});
  }
}
constraints = [{'offsets': [{'node': '0', 'offset': '0'}], 'type': 'alignment', 'axis': 'x'}, {'offsets': [{'node': '1', 'offset': '0'}, {'node': '2', 'offset': '0'}, {'node': '3', 'offset': '0'}, {'node': '4', 'offset': '0'}, {'node': '5', 'offset': '0'}, {'node': '6', 'offset': '0'}, {'node': '7', 'offset': '0'}], 'type': 'alignment', 'axis': 'x'}, {'offsets': [{'node': '8', 'offset': '0'}, {'node': '9', 'offset': '0'}, {'node': '10', 'offset': '0'}, {'node': '11', 'offset': '0'}, {'node': '12', 'offset': '0'}], 'type': 'alignment', 'axis': 'x'}, {'offsets': [{'node': '13', 'offset': '0'}], 'type': 'alignment', 'axis': 'x'}]
lks = [{'source': 0, 'target': 1, 'weight': 1}, {'source': 0, 'target': 2, 'weight': 1}, {'source': 0, 'target': 3, 'weight': 1}, {'source': 0, 'target': 4, 'weight': 1}, {'source': 0, 'target': 5, 'weight': 1}, {'source': 0, 'target': 6, 'weight': 1}, {'source': 0, 'target': 7, 'weight': 1}, {'source': 1, 'target': 8, 'weight': 10}, {'source': 3, 'target': 8, 'weight': 1}, {'source': 5, 'target': 8, 'weight': 5}, {'source': 7, 'target': 8, 'weight': 7}, {'source': 1, 'target': 9, 'weight': 9}, {'source': 2, 'target': 9, 'weight': 8}, {'source': 4, 'target': 9, 'weight': 6}, {'source': 5, 'target': 9, 'weight': 9}, {'source': 6, 'target': 9, 'weight': 5}, {'source': 7, 'target': 9, 'weight': 8}, {'source': 2, 'target': 10, 'weight': 1}, {'source': 3, 'target': 10, 'weight': 5}, {'source': 4, 'target': 10, 'weight': 2}, {'source': 5, 'target': 10, 'weight': 5}, {'source': 6, 'target': 10, 'weight': 10}, {'source': 7, 'target': 10, 'weight': 4}, {'source': 1, 'target': 11, 'weight': 1}, {'source': 2, 'target': 11, 'weight': 2}, {'source': 3, 'target': 11, 'weight': 5}, {'source': 5, 'target': 11, 'weight': 9}, {'source': 6, 'target': 11, 'weight': 4}, {'source': 7, 'target': 11, 'weight': 4}, {'source': 1, 'target': 12, 'weight': 7}, {'source': 3, 'target': 12, 'weight': 5}, {'source': 4, 'target': 12, 'weight': 8}, {'source': 7, 'target': 12, 'weight': 3}, {'source': 12, 'target': 13, 'weight': 6}, {'source': 12, 'target': 13, 'weight': 12}, {'source': 12, 'target': 13, 'weight': 18}, {'source': 12, 'target': 13, 'weight': 24}, {'source': 11, 'target': 13, 'weight': 9}, {'source': 11, 'target': 13, 'weight': 18}, {'source': 11, 'target': 13, 'weight': 27}, {'source': 11, 'target': 13, 'weight': 36}, {'source': 10, 'target': 13, 'weight': 1}, {'source': 10, 'target': 13, 'weight': 2}, {'source': 10, 'target': 13, 'weight': 3}, {'source': 10, 'target': 13, 'weight': 4}, {'source': 9, 'target': 13, 'weight': 9}, {'source': 9, 'target': 13, 'weight': 18}, {'source': 9, 'target': 13, 'weight': 27}, {'source': 9, 'target': 13, 'weight': 36}, {'source': 8, 'target': 13, 'weight': 1}, {'source': 8, 'target': 13, 'weight': 2}, {'source': 8, 'target': 13, 'weight': 3}, {'source': 8, 'target': 13, 'weight': 4}]
solns = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [3, 8], [5, 8], [6, 9], [2, 10], [4, 10], [7, 10], [1, 11], [11, 13], [10, 13], [10, 13], [10, 13], [9, 13], [8, 13], [8, 13]]
