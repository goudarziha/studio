import React from "react";
import ReactDOM from "react-dom";
import Video from "./Video";
import Gallery from "./Gallery";
import Main from "./layouts/Main";
import { Route, HashRouter as Router, Switch } from "react-router-dom";

import { Provider } from "react-redux";
import store from "../store";
import Modal from "react-modal";

Modal.setAppElement("#app");

const routing = (
  <Provider store={store}>
    <Router>
      <div className="container">
        <Switch>
          <Route exact path="/" component={Video} />
          <Route exact path="/gallery" component={Gallery} />
        </Switch>
      </div>
    </Router>
  </Provider>
);

ReactDOM.render(routing, document.getElementById("app"));
