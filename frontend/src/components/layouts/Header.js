import React, { Component } from "react";
import { Link, Switch } from "react-router-dom";

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <a className="navbar-brand" href="#">
          STUDIO
        </a>
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link to="/">Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/gallery">Gallery</Link>
          </li>
        </ul>
      </nav>
    );
  }
}

export default Header;
