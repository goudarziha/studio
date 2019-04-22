import GET_GALLERY from "./Types";
import axios from "axios";

export function getGallery() {
  return function(dispatch) {
    return axios.get("/api/media").then(res => {
      dispatch({
        type: GET_GALLERY,
        payload: res.data
      });
    });
  };
}
