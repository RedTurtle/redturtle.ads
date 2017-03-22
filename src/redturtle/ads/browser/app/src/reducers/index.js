import * as types from '../constants/ActionTypes';

const initialState = {
  data: [],
  pagination: {},
  searchableText: '',
};

const searchResults = (state=initialState, action) => {
  switch (action.type) {
    case types.RECEIVE_SEARCH_RESULTS:
      return Object.assign({}, state, {
          data: action.searchResults.data,
          pagination: {
            links: action.searchResults.links,
            infos: action.searchResults.meta,
          },
        });
    case types.UPDATE_SEARCHABLE_TEXT:
      return Object.assign({}, state, { searchableText: action.searchableText });
    default:
      return state;
  }
};

export default searchResults;
