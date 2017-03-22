import './index.css';
import { createStore, applyMiddleware } from 'redux';
import { getSearchResults } from './actions';
import { Provider } from 'react-redux';
import App from './App';
import createLogger from 'redux-logger';
import React from 'react';
import ReactDOM from 'react-dom';
import reducer from './reducers';
import thunk from 'redux-thunk';

const middleware = [thunk];
if (process.env.NODE_ENV !== 'production') {
  middleware.push(createLogger());
};

const store = createStore(
  reducer,
  applyMiddleware(...middleware)
);

store.dispatch(getSearchResults());

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('advertisements-wrapper')
);
