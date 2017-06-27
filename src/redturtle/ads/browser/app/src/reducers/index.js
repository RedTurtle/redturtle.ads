import * as types from '../constants/ActionTypes';

const initialState = {
  data: [],
  pagination: {},
  searchableText: '',
  searchableCategory: '',
};

const searchResults = (state=initialState, action) => {
  switch (action.type) {
    case types.RECEIVE_SEARCH_RESULTS:
      return Object.assign({}, state, {
          data: action.data,
          pagination: {
            links: action.data.links,
            infos: action.data.meta,
          },
        });

    case types.UPDATE_SEARCHABLE_TEXT:
      return Object.assign({}, state, { searchableText: action.searchableText });

    case types.UPDATE_SEARCHABLE_CATEGORY:
      return Object.assign({}, state, { searchableCategory: action.searchableCategory });

    default:
      return state;
  }
};

export default searchResults;
