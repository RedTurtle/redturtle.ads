import React, { Component } from 'react';
import { changedSearchableText, getSearchResults } from '../actions';
import { connect } from 'react-redux';
import Command from '../components/Command';

// import Content from '../components/Content';

export class SearchFiltersContainer extends Component {

  render() {

    const { changedSearchableText, getSearchResults } = this.props;

    const submittedSearch = (e) => {
      e.preventDefault();
      return getSearchResults();
    };

    return (
      <div className="filters-container">
        <form className="form-inline"
              onSubmit={submittedSearch}>
          <div className="form-group">
            <input type="search"
                   className="form-control"
                   id="searchableText"
                   placeholder="Search"
                   onChange={changedSearchableText}
                   name="searchableText" />
          </div>
          <Command onClick={submittedSearch} />
        </form>
      </div>
    );
  }
}

export default connect((state) => state, { changedSearchableText, getSearchResults })(SearchFiltersContainer);
