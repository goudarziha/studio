import React, { Component } from "react";
import RecordRTC from "recordrtc";
import axios from "axios";
import Header from "../components/layouts/Header";

class Video extends Component {
  constructor(props) {
    super(props);

    this.video = React.createRef();
  }
  state = {
    stream: null,
    url: "",
    videoRecorder: "",
    isRecording: false,
    isUploading: false,
    isRendering: false,
    isPreview: false,
    isDone: false,
    pausing: false
  };

  componentDidMount() {
    this.setState({
      videoRecorder: null
    });
  }

  setup() {
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
          const videoRecorder = RecordRTC(stream, {
            type: "video",
            video: {
              width: 1280,
              height: 720,
              frameRate: { exact: 60 },
              videoBitsPerSecond: 51200000,
              mimeType: "video/webm"
            }
          });
          const vid = document.getElementById("video");
          vid.srcObject = stream;
          this.setState({
            stream: stream,
            videoRecorder: videoRecorder
          });
        },
        err => {
          console.log(err.name);
        }
      );
    }
  }

  componentDidMount() {
    this.setup();
  }

  handleStartRecord() {
    console.log("START RECORDING");
    console.log(this.state.videoRecorder);
    this.state.videoRecorder.startRecording();
    this.setState({
      isRecording: true
    });
    setTimeout(
      function() {
        this.stopRecording();
        this.uploadFile().then(response => {
          console.log(response);
        });
      }.bind(this),
      12000
    );
  }

  stopRecording() {
    console.log("STOP RECORDING");
    this.state.videoRecorder.stopRecording(url => {
      this.setState({
        isRecording: false,
        pausing: false,
        hasRecording: true,
        isRendering: true
      });
    });
  }

  convertBase64ToFile(image) {
    const byteString = atob(image.split(",")[1]);
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i += 1) {
      ia[i] = byteString.charCodeAt(i);
    }
    const newBlob = new Blob([ab], {
      type: "image/webm"
    });
    return newBlob;
  }

  uploadFile() {
    this.state.videoRecorder.getDataURL(data => {
      if (data) {
        console.log("HEs");
        console.log(data);
        const formData = new FormData();
        formData.append("file", this.convertBase64ToFile(data));
        axios
          .post("/api/media", formData)
          .then(res => {
            console.log(res);
            this.setState({
              isRendering: false
            });
          })
          .catch(err => {
            console.log(err);
          });
      }
    });
  }

  render() {
    return (
      <div className="container">
        <Header />
        <video id="video" className="video" autoPlay muted />
        {!this.state.isRecording && (
          <button onClick={this.handleStartRecord.bind(this)}>Record</button>
        )}
        {this.state.isRecording && <h2>Recording</h2>}
        {this.state.isRendering && <h2>Rendering</h2>}
      </div>
    );
  }
}

export default Video;
