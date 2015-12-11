var React = window.React = require('react'),
    ReactDOM = require("react-dom"),
    Attendance = require("./components/Attendance"),
    mountNode = document.getElementById("app"); 

ReactDOM.render(<Attendance />, mountNode);