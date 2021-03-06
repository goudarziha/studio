import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getGallery, postEmail } from "../actions/galleryActions";
import Modal from "react-modal";

import "./Gallery.css";

export class Gallery extends Component {
  state = {
    url: "",
    showModal: false,
    email: "",
    selectedId: null
  };
  static propTypes = {
    getGallery: PropTypes.func.isRequired,
    gallery: PropTypes.any.isRequired,
    postEmail: PropTypes.func.isRequired
  };
  componentDidMount() {
    this.props.getGallery();
    this.timer = setInterval(() => this.props.getGallery(), 10000);

    const protocol = window.location.protocol;
    const domain = window.location.hostname;
    const port = window.location.port;

    this.setState({
      url: protocol + "//" + domain + ":" + port + "/"
    });

    navigator.getUserMedia =
      navigator.getUserMedia ||
      navigator.webkitGetUserMedia ||
      navigator.mozGetUserMedia;

    if (navigator.getUserMedia) {
      navigator.getUserMedia(
        {
          audio: true,
          video: {
            height: 720,
            width: 1280
          }
        },
        stream => {
          stream.getTracks[0].stop();
        },
        err => {
          console.log(err.name);
        }
      );
    }
  }

  componentWillUnmount() {
    this.timer = null;
  }

  handleClick = id => {
    this.showModal();
    this.setState({
      selectedId: id
    });
  };

  showModal() {
    this.setState({
      showModal: true
    });
  }

  hideModal() {
    this.setState({
      showModal: false,
      email: "",
      selectedId: null
    });
  }

  onEmailSubmit = e => {
    e.preventDefault();
    console.log(this.state);
    const { selectedId, email } = this.state;
    this.props.postEmail(selectedId, email);
    this.setState({
      email: "",
      selectedId: null,
      showModal: false
    });
  };

  handleChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  render() {
    const customStyles = {
      content: {
        top: "50%",
        left: "50%",
        right: "auto",
        bottom: "auto",
        marginRight: "-50%",
        transform: "translate(-50%, -50%)"
      }
    };

    return (
      <div>
        <div className="d-flex justify-content-center m-5">
          <h2>GALLERY</h2>
        </div>

        <Modal
          isOpen={this.state.showModal}
          onRequestClose={this.hideModal.bind(this)}
          style={customStyles}
        >
          <div className="w-100">
            <div className="d-flex flex-column justify-content-start w-100">
              <h4>Enter Your Email</h4>
              <form onSubmit={this.onEmailSubmit} className="mt-3 pt-3">
                <div className="form-group">
                  <label htmlFor="email" className="">
                    Email
                  </label>
                  <input
                    type="email"
                    name="email"
                    onChange={this.handleChange}
                  />
                </div>

                <div className="d-flex justify-content-end mt-5">
                  <button
                    onClick={this.hideModal.bind(this)}
                    className="btn btn-danger pr-3"
                  >
                    Cancel
                  </button>

                  <button type="submit" className="btn btn-secondary ml-3">
                    Submit
                  </button>
                </div>
              </form>
            </div>
          </div>
        </Modal>

        <div className="gallery">
          {this.props.gallery
            .map(item => (
              <div
                className="gallery__item"
                key={item.id}
                onClick={() => this.handleClick(item.id)}
              >
                <video
                  className="gallery__video"
                  autoPlay
                  loop
                  muted
                  key={item.id}
                  src={[this.state.url + "static/" + item.file_url].toString()}
                />
              </div>
            ))
            .reverse()}
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
  { getGallery, postEmail }
)(Gallery);
