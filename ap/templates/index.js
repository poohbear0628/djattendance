/*
 * Base npm struture for entire website
 * Add any libraries that can be installed by npm here.
 *
 * Goal is to have one large javascript file for the entire
 * site. That way we can use caching to our advantage to
 * speed up site load.
 */

var $ = require('jquery');
window.$ = $;
window.jQuery = $;
require('bootstrap-sass');
var attachFastClick = require('fastclick');
// Add fast click to remove click delay on mobile
attachFastClick(document.body);

//JSZip 2.5.0, pdfmake 0.1.18,
// Datatables import
import dt from 'datatables.net';
require('datatables.net-buttons')(window, $);
require('datatables.net-buttons-bs')(window, $);
require('datatables.net-buttons/js/buttons.colVis.js')(); // Column visibility
require('datatables.net-buttons/js/buttons.html5.js')();  // HTML 5 file export
require('datatables.net-buttons/js/buttons.flash.js')();  // Flash file export
require('datatables.net-buttons/js/buttons.print.js')();  // Print view button
require('datatables.net-select')(window, $);
require('datatables.net-fixedheader')(window, $);
require('datatables.net-scroller')(window, $);

var autosize = require('autosize');

$(document).ready(function(){
  // Makes all textarea elastic (resize according to content)
  autosize($('textarea'));
});

// CSS imports
import 'bootstrap-sass/assets/stylesheets/_bootstrap.scss';
import 'datatables.net-bs/css/dataTables.bootstrap.css';