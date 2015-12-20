import React from 'react'
import { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import Attendance from './containers/Attendance'
import attendance from './reducers'
import initialState from './initialState'


const store = (window.devToolsExtension ? window.devToolsExtension()
                (createStore) : createStore)(attendance, initialState)

let rootElement = document.getElementById('root')
render(
  <Provider store={store}>
    <Attendance />
  </Provider>,
  rootElement
)

// var React = window.React = require('react'),
//     ReactDOM = require("react-dom"),
//     Router = require('react-router').Router,
//     Provider = require('react-redux').Provider,
//     store = require('./store'),
//     routes = require('./routes');

// ReactDom.render(
//     <Provider store={store}>
//         <Router routes={routes}/>
//     </Provider>,
//     document.getElementById('root')
// );

    // Attendance = require("./components/Attendance"),
    // mountNode = document.getElementById("app"); 

// ReactDOM.render(<Attendance />, mountNode);