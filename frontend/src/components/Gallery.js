import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import getGallery from "../actions/galleryActions";

export class Gallery extends Component {
  static propTypes = {
    getGallery: PropTypes.func.isRequired
  };
  componentDidMount() {
    // this.props.getGallery();
    console.log(this.props);
  }
  render() {
    return (
      <div>
        <h2>GALLERY</h2>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getGallery: dispatch(getGallery())
  };
};
export default connect()(Gallery);
