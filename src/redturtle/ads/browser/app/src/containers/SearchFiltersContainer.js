import React, { Component } from 'react';
import { changedSearchableText, changedSearchableCategory, getSearchResults } from '../actions';
import { connect } from 'react-redux';
import Command from '../components/Command';
import axios from 'axios';

// import Content from '../components/Content';

export class SearchFiltersContainer extends Component {

    constructor(props) {
      super(props);
      this.state = {
          categories: []
      };
    }

    componentDidMount() {
      const apiUrl = document.body.dataset.portalUrl;
      axios.get(apiUrl + '/search_categories',
      {
        responseType: 'json',
      })
      .then((result)=> {
        this.setState({
          categories: result.data
        });
      })
    };

    submittedSearch = (e) => {
      e.preventDefault();
      return this.props.getSearchResults();
    };

    handleChange = (e) => {
      this.props.changedSearchableCategory(e);
      this.submittedSearch(e);
    }


  render() {
    const theData = this.state.categories;
    let renderSelect = theData.map((category) => {
        return <option key={category.id} value={category.uid}>{category.title}</option>
    });
    const { changedSearchableText } = this.props;


    return (
      <div className="filters-container">
        <select onChange={this.handleChange}>
            {renderSelect}
        </select>

        <form className="form-inline"
              onSubmit={this.submittedSearch}>
          <div className="form-group">
            <input type="search"
                   className="form-control"
                   id="searchableText"
                   placeholder="Search"
                   onChange={changedSearchableText}
                   name="searchableText" />
          </div>
          <Command onClick={this.submittedSearch} />
        </form>
      </div>
    );
  }
}

export default connect((state) => state, { changedSearchableText, changedSearchableCategory, getSearchResults })(SearchFiltersContainer);
