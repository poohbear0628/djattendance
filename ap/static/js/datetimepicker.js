$(document).ready(function() {
  $(".datetimepicker").datetimepicker({
    format: "m/d/Y H:i A",
    formatTime: "H:i A",
    ampm: false,
    step: 30,
    defaultSelect: false,
    allowBlank: false,
    validateOnBlur: false
  });
});
