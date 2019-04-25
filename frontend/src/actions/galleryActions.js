import {
  GET_GALLERY,
  POST_MEDIA,
  POST_EMAIL,
  POST_EMAIL_SUCCESS,
  POST_EMAIL_FAIL
} from "./Types";
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

export const postEmail = (media_id, email) => dispatch => {
  dispatch({ type: POST_EMAIL });

  axios
    .post("/api/email", { media_id, email })
    .then(res => {
      dispatch(postEmailSuccess(res.data));
    })
    .catch(err => {
      dispatch(postEmailFail(err));
      console.log(err);
    });
};

export const postEmailSuccess = data => dispatch => {
  dispatch({
    type: POST_EMAIL_SUCCESS,
    payload: data
  });
};

export const postEmailFail = err => dispatch => {
  dispatch({
    type: POST_EMAIL_FAIL,
    payload: err
  });
};
