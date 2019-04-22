import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from "./layouts/Header";
import Video from "./Video";
import Gallery from "./Gallery";
import Main from "./layouts/Main";
import { Route, Link, BrowserRouter as Router, Switch } from "react-router-dom";
import { createStore, applyMiddleware } from "redux";

import { Provider } from "react-redux";
import thunk from "redux-thunk";
import rootReducer from "../reducers";

const store = createStore(rootReducer, applyMiddleware(thunk));

const routing = (
  <Provider store={store}>
    <Router>
      <div className="container">
        <Header />
        <Switch>
          <Route exact path="/" component={Main} />
          <Route path="/gallery" component={Gallery} />
        </Switch>
      </div>
    </Router>
  </Provider>
);

ReactDOM.render(routing, document.getElementById("app"));
