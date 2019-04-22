import { combineReducers } from "redux";
import galleryReducer from "./galleryReducer";

export default combineReducers({ gallery: galleryReducer });
