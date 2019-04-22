import { GET_GALLERY } from "../actions/Types";

const initalState = {
  gallery: []
};

const galleryReducer = (state = initalState, action) => {
  switch (action.type) {
    case GET_GALLERY:
      return {
        ...state,
        gallery: action.payload.data
      };
    default:
      return state;
  }
};

export default galleryReducer;
