// Import TinyMCE
var tinymce = require('tinymce/tinymce');

// A theme is also required
require('tinymce/themes/modern/theme');

// Any plugins you want to use has to be imported
require('tinymce/plugins/paste');
require('tinymce/plugins/link');

//tinymce skins import
require.context(
  'file?name=[path][name].[ext]&context=node_modules/tinymce!tinymce/skins',
  true,
  /.*/
);


// Initialize the app
tinymce.init({
  selector: 'textarea.mceEditor',
  plugins: ['paste', 'link']
});

