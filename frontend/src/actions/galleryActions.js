import { GET_GALLERY, POST_MEDIA } from "./Types";
import axios from "axios";

export const getGallery = () => dispatch => {
  axios
    .get("/api/media")
    .then(res => {
      dispatch({
        type: GET_GALLERY,
        payload: res.data
      });
    })
    .catch(err => {
      console.log(err);
    });
};

export const postGallery = (galleryId, file) => dispatch => {
  axios
    .post("/api/media", { id: galleryId, file: file })
    .then(res => {
      dispatch({ type: POST_MEDIA, payload: res.data });
    })
    .catch(err => {
      console.log(err);
    });
};
