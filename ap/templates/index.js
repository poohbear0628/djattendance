/*
 * Base npm struture for entire website
 * Add any libraries that can be installed by npm here.
 *
 * Goal is to have one large javascript file for the entire
 * site. That way we can use caching to our advantage to
 * speed up site load.
 */

/**************************
* expose global libraries *
**************************/
require('expose-loader?moment!moment');
require('expose-loader?$!expose-loader?jQuery!jquery');
require('expose-loader?Countable!countable');
require('expose-loader?Dropzone!dropzone'); require('dropzone/dist/dropzone.css');
require('expose-loader?_!underscore');
require('expose-loader?xolor!xolor');
require('expose-loader?fastclick!fastclick');
require('expose-loader?autosize!autosize/dist/autosize');

/**********************************
* load plugins and respective css *
**********************************/
require('fullcalendar'); require('fullcalendar/dist/fullcalendar.css');
require('jquery.shorten/src/jquery.shorten');
require('devbridge-autocomplete');
require('selectize'); require('selectize/dist/css/selectize.default.css');
require('bootstrap-sass'); require('bootstrap-sass/assets/stylesheets/_bootstrap.scss');
require('bootstrap-toggle'); require('bootstrap-toggle/css/bootstrap-toggle.css');
require('pdfmake/build/pdfmake');
require('pdfmake/build/vfs_fonts.js');
// Datatables import, see https://datatables.net/forums/discussion/39648/datatable-buttons-not-working-on-webpack
require("datatables.net");
require("datatables.net-bs"); require('datatables.net-bs/css/dataTables.bootstrap.css');
require("datatables.net-buttons");
require("datatables.net-buttons-bs"); require('datatables.net-buttons-bs/css/buttons.bootstrap.css');
require('datatables.net-buttons/js/buttons.colVis');
require('datatables.net-buttons/js/buttons.html5');
require('datatables.net-buttons/js/buttons.flash');
require('datatables.net-buttons/js/buttons.print');
require('datatables.net-select'); require('datatables.net-select-bs/css/select.bootstrap.css');
require('datatables.net-fixedheader'); require('fullcalendar/dist/fullcalendar.css');
require('datatables.net-scroller'); require('datatables.net-scroller-bs/css/scroller.bootstrap.css');
require('jquery-ui'); require('jquery-ui/themes/base/all.css');
require('jquery-ui/ui/widgets/datepicker');
require('jquery-seat-charts'); require('jquery-seat-charts/jquery.seat-charts.css');
// select2 js handeled by django_select2
require('select2/select2.css');

/***************
* Custom files *
***************/
require('bootflat-ftta/bootflat/scss/bootflat.scss');
require('ap/css/jquery.autocomplete.css');
require('ap/css/select2-bootstrap.css');
require('ap/css/base.css');
require('ap/offcanvas/offcanvas'); require('ap/offcanvas/offcanvas.css');
require('ap/js/init');
