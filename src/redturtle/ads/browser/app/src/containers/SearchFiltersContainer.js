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
          categories: [],
          strings: {}
      };
    }

    componentDidMount() {
      const apiUrl = document.body.getAttribute('data-portal-url');
      axios.get(apiUrl + '/search_categories',
      {
        responseType: 'json',
      })
      .then((result)=> {
        this.setState({
          categories: result.data
        });
      })
      axios.get(apiUrl + '/translate_string',
      {
        responseType: 'json',
      })
      .then((result)=> {
        this.setState({
          strings: result.data
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
    let SelectCategory = null;
    const theData = this.state.categories;
    let renderSelect = theData.map((category) => {
        return <option key={category.id} value={category.path}>{category.title}</option>
    });
    const { changedSearchableText } = this.props;

    let isCat = document.getElementsByTagName("body")[0].className.match('portaltype-adscategory')?true:false
    if (!isCat){
        SelectCategory = (
            <select onChange={this.handleChange}>
                {renderSelect}
            </select>
        );
    }
    else{
        SelectCategory = '';
    }


    return (
      <div className="filters-container">
        {SelectCategory}

        <form className="form-inline"
              onSubmit={this.submittedSearch}>
            <input type="search"
                   className="form-control"
                   id="searchableText"
                   placeholder={this.state.strings.search}
                   onChange={changedSearchableText}
                   name="searchableText" />
          <Command onClick={this.submittedSearch} />
        </form>
      </div>
    );
  }
}

export default connect((state) => state, { changedSearchableText, changedSearchableCategory, getSearchResults })(SearchFiltersContainer);
