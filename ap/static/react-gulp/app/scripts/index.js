import React from 'react'
import { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import Attendance from './containers/Attendance'
import reducer from './reducers/reducer'
import initialState from './initialState'

const store = (window.devToolsExtension ? window.devToolsExtension()
                (createStore) : createStore)(reducer, initialState);
                
let rootElement = document.getElementById('root');
render(
  <Provider store={store}>
    <Attendance />
  </Provider>,
  rootElement
);