/*
 * Base npm struture for entire website
 * Add any libraries that can be installed by npm here.
 *
 * Goal is to have one large javascript file for the entire
 * site. That way we can use caching to our advantage to
 * speed up site load.
 */

window.moment = require('moment')

var $ = require('jquery');
//Expose jQuery to global
window.$ = $;
window.jQuery = $;

require('bootstrap-sass');
require('expose-loader?Countable!countable');

// Add fast click to remove click delay on mobile
var attachFastClick = require('fastclick');
attachFastClick.attach(document.body);

// Datatables import
// https://datatables.net/forums/discussion/39648/datatable-buttons-not-working-on-webpack
import "datatables.net";
import "datatables.net-bs";
import "datatables.net-buttons";
import "datatables.net-buttons-bs";
import 'datatables.net-buttons/js/buttons.colVis.js';
import 'datatables.net-buttons/js/buttons.html5.js';
import 'datatables.net-buttons/js/buttons.flash.js';
import 'datatables.net-buttons/js/buttons.print.js';
import 'datatables.net-select';
import 'datatables.net-fixedheader';
import 'datatables.net-scroller';

// PDFmake for pdf export datatables
require('pdfmake/build/pdfmake');
require('pdfmake/build/vfs_fonts.js');

var autosize = require('autosize/dist/autosize.js');
$(document).ready(function(){
  // Makes all textarea elastic (resize according to content)
  autosize($('textarea'));
});

// CSS imports
import 'bootstrap-sass/assets/stylesheets/_bootstrap.scss';
import 'datatables.net-bs/css/dataTables.bootstrap.css';
import 'datatables.net-buttons-bs/css/buttons.bootstrap.css';
import 'datatables.net-select-bs/css/select.bootstrap.css';
import 'datatables.net-fixedheader-bs/css/fixedHeader.bootstrap.css';
import 'datatables.net-scroller-bs/css/scroller.bootstrap.css';
import 'bootflat-ftta/bootflat/scss/bootflat.scss'

// Select2 imports
import '../static/libraries/bootstrap-select2/select2-bootstrap.css';
import '../static/libraries/bootstrap-select2/select2-django.js';
require('select2/select2.css');

window._ = require('underscore');

window.Dropzone = require('dropzone');
require('dropzone/dist/dropzone.css');

require('selectize');
require('selectize/dist/css/selectize.default.css');

require('bootstrap-toggle');
require('bootstrap-toggle/css/bootstrap-toggle.css');

window.xolor = require('xolor');
