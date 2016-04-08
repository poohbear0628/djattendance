import React from 'react'
import { render } from 'react-dom'
import { createStore, applyMiddleware, compose } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { Provider } from 'react-redux'
import Attendance from './containers/Attendance'
import reducer from './reducers/reducer'
import initialState from './initialState'

const store = createStore(reducer, initialState, compose(
    applyMiddleware(thunkMiddleware),
    window.devToolsExtension ? window.devToolsExtension() : f => f //redux chrome dev tools
  ));

let rootElement = document.getElementById('root');
render(
  <Provider store={store}>
    <Attendance />
  </Provider>,
  rootElement
);