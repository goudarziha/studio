import { GET_GALLERY } from "../actions/Types";

const initalState = {};

const galleryReducer = (state = initalState, action) => {
  switch (action.type) {
    case GET_GALLERY:
      return {
        gallery: action.payload
      };
    default:
      return state;
  }
};

export default galleryReducer;
