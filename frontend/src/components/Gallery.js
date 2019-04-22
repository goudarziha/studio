import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getGallery } from "../actions/galleryActions";

export class Gallery extends Component {
  static propTypes = {
    getGallery: PropTypes.func.isRequired,
    gallery: PropTypes.any.isRequired
  };
  componentDidMount() {
    this.props.getGallery();
    this.timer = setInterval(() => this.props.getGallery(), 10000);
  }

  componentWillUnmount() {
    this.timer = null;
  }

  handleClick = id => {
    console.log(id);
  };

  render() {
    return (
      <div>
        <h2>GALLERY</h2>

        <div className="row">
          {this.props.gallery.map(item => (
            <div
              className="col-md-3 m-3"
              key={item.id}
              onClick={() => this.handleClick(item.id)}
            >
              <video
                width="200px"
                height="200px"
                autoPlay
                loop
                muted
                key={item.id}
                src={[
                  "http://localhost:5000/static/" + item.file_url
                ].toString()}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  gallery: state.gallery.gallery
});

export default connect(
  mapStateToProps,
  { getGallery }
)(Gallery);
