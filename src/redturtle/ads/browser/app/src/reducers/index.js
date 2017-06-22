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
          data: action.data,
          pagination: {
            links: action.data.links,
            infos: action.data.meta,
          },
        });
    case types.UPDATE_SEARCHABLE_TEXT:
      return Object.assign({}, state, { searchableText: action.searchableText });
    default:
      return state;
  }
};

export default searchResults;
