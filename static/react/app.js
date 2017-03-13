import { Router,Route } from 'react-router'
import createBrowserHistory from 'history/createBrowserHistory'
import Todo from "./components/Todo"
import ReactDOM from 'react-dom';
import React from 'react';
import {index_api} from "./config/api"
const history = createBrowserHistory()

const routes = (
  <Router history={history}>
    <Route path="/" component={Todo} />
  </Router>
);

ReactDOM.render(routes, document.getElementById('app'));
