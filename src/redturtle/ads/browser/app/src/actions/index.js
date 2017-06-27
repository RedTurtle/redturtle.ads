import * as types from '../constants/ActionTypes';
import axios from 'axios';

export const receiveSearchResults = (searchResults) => ({
  type: types.RECEIVE_SEARCH_RESULTS,
  data: searchResults,
});

export const updateSearchableText = (text) => ({
  type: types.UPDATE_SEARCHABLE_TEXT,
  searchableText: text,
});

export const updateSearchableCategory = (category) => ({
  type: types.UPDATE_SEARCHABLE_CATEGORY,
  searchableCategory: category,
});

export const unableContactBackend = (error) => ({
  type: types.UNABLE_CONTACT_BACKEND,
  error: error,
});

const generateQuery = (state, pageNumber) => {
  const wrapper = document.getElementById('advertisements-wrapper');

  let params = {};

  if (wrapper.dataset.path) {
    params.path = wrapper.dataset.path;
  }

  if (state.searchableText.length > 0) {
    params.q = state.searchableText;
  }

  if (state.searchableCategory.length > 0) {
    params.path = state.searchableCategory;
  }

  if (pageNumber) {
    params.b_start = pageNumber * state.pagination.infos.pageSize;
  }

  return params;
};

export const getSearchResults = (pageNumber) => (dispatch, getState) => {
  const apiUrl = document.body.dataset.portalUrl;
  const state = getState();

  axios.get(
    apiUrl + '/search_advertisements',
    {
      params: generateQuery(state, pageNumber),
      responseType: 'json',
    }
  ).then(response => {
      return dispatch(receiveSearchResults(response.data?response.data:[]));
  });
};

export const changedSearchableText = (e) => dispatch => dispatch(updateSearchableText(e.target.value));
export const changedSearchableCategory = (e) => dispatch => dispatch(updateSearchableCategory(e.target.value));
