import {
  GET_GALLERY,
  POST_EMAIL,
  POST_EMAIL_SUCCESS,
  POST_EMAIL_FAIL
} from "../actions/Types";

const initalState = {
  gallery: []
};

const galleryReducer = (state = initalState, action) => {
  switch (action.type) {
    case GET_GALLERY:
      // TODO FIND THE DIFFERENCE IN BOTH ARRAYS, APPEND ONLY DIFFERENCE
      return {
        ...state,
        gallery: action.payload.data
      };
    case POST_EMAIL:
      return state;
    case POST_EMAIL_SUCCESS:
      return state;
    case POST_EMAIL_FAIL:
      return state;
    default:
      return state;
  }
};

export default galleryReducer;
