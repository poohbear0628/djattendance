import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'

import { applyMiddleware, combineReducers, compose, createStore } from 'redux'
import {reducer as formReducer} from 'redux-form';
import thunkMiddleware from 'redux-thunk'

import Attendance from './containers/Attendance'
import combined from './reducers/reducer'
import initialState from './initialstate'

// const reducers = {
//   reducer: reducer,
//   form: formReducer
// }

// const combined = combineReducers(reducers);

const store = createStore(combined, initialState, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f //redux chrome dev tools
));

console.log(store.getState());

let rootElement = document.getElementById('root');

render(
  <Provider store={store}>
    <Attendance />
  </Provider>,
  rootElement
);