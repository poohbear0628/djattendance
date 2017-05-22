import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { applyMiddleware, combineReducers, compose, createStore } from 'redux'
import {reducer as formReducer} from 'redux-form'
import thunkMiddleware from 'redux-thunk'
import { AppContainer } from 'react-hot-loader'

import Attendance from './containers/Attendance'
import combined from './reducers/reducer'
import initialState from './initialstate'

// scss imports
import '../scss/react-calendar.scss'
import '../scss/index.css'
import 'font-awesome/scss/font-awesome.scss'
import 'react-select/scss/default.scss'
import 'react-widgets/dist/css/react-widgets.css'

const store = createStore(combined, initialState, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f //redux chrome dev tools
));

let rootElement = document.getElementById('root');

const render = (Component) => {
  ReactDOM.render(
    <AppContainer>
      <Provider store={store}>
        <Component />
      </Provider>
    </AppContainer>,
    rootElement
  )
}

render(
  Attendance
)

if (module.hot) {
  module.hot.accept('./containers/Attendance', () => {
    render(Attendance)
  });
}
