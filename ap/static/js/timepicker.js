$(document).ready(function() {
  $(".timepicker").datetimepicker({
    format: "H:i A",
    formatTime: "H:i A",
    ampm: true,
    step: 30,
    defaultSelect: false,
    allowBlank: false,
    validateOnBlur: false,
    datepicker:false,
  });
});
