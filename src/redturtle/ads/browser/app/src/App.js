import React, { Component } from 'react';
import './App.css';
import SearchFiltersContainer from './containers/SearchFiltersContainer';
import SearchResultsContainer from './containers/SearchResultsContainer';
import AddNewAdvertisementContainer from './containers/AddNewAdvertisementContainer';

class App extends Component {
  render() {
    return (
      <div className="advertisements-wrapper">
      <SearchFiltersContainer />
      <SearchResultsContainer data={this.props.data} />
      </div>
    );
  }
}

export default App;
