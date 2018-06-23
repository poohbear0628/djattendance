// Import TinyMCE
// see https://github.com/fyrkant/simple-tinymce-webpack
// see https://www.tinymce.com/docs/advanced/usage-with-module-loaders/#webpackfile-loader
import tinymce from "tinymce/tinymce";

// A theme is also required
import "tinymce/themes/modern";

// Any plugins you want to use has to be imported
//"advlist autolink autosave link image lists charmap print preview hr anchor pagebreak",
import "tinymce/plugins/advlist";
import "tinymce/plugins/autolink";
import "tinymce/plugins/autosave";
import "tinymce/plugins/link";
import "tinymce/plugins/image";
import "tinymce/plugins/lists";
import "tinymce/plugins/charmap";
import "tinymce/plugins/print";
import "tinymce/plugins/preview";
import "tinymce/plugins/hr";
import "tinymce/plugins/anchor";
import "tinymce/plugins/pagebreak";

//"searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
import "tinymce/plugins/searchreplace";
import "tinymce/plugins/wordcount";
import "tinymce/plugins/visualblocks";
import "tinymce/plugins/visualchars";
import "tinymce/plugins/code";
import "tinymce/plugins/fullscreen";
import "tinymce/plugins/insertdatetime";
import "tinymce/plugins/media";
import "tinymce/plugins/nonbreaking";

//"table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
import "tinymce/plugins/table";
import "tinymce/plugins/contextmenu";
import "tinymce/plugins/directionality";
import "tinymce/plugins/emoticons";
import "tinymce/plugins/template";
import "tinymce/plugins/textcolor";
import "tinymce/plugins/paste";
//import "tinymce/plugins/fullpage";
import "tinymce/plugins/colorpicker";
import "tinymce/plugins/textpattern";


let pluginStr = "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak " +
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking " +
    "table contextmenu directionality emoticons template textcolor paste textcolor colorpicker textpattern";

let pluginList = pluginStr.split(" ");

require.context(
  "file-loader?name=[path][name].[ext]&context=node_modules/tinymce!tinymce/skins",
  true,
  /.*/
);

tinymce.init({
  selector: 'textarea',
  plugins: pluginStr,
  // setup (editor) {
  //   editor.on('keyup', e => console.log(editor.getContent()))
  // }
});

// Initialize
tinymce.init({
  selector: '.editor',
  theme: 'lightgray',
  inline: true,
  // setup (editor) {
  //   editor.on('keyup', e => console.log(editor.getContent()))
  // }
});


// tinymce.init({
//   height: 500,
//   plugins: pluginList,
//   selector:"textarea",
// });

