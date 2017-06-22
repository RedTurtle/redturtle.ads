import React, { Component } from 'react';
// import Command from '../components/Command';
import CategoriesList from '../containers/CategoriesList';

// import Content from '../components/Content';

export default class AddNewAdvertisementContainer extends Component {

  render() {
    return (
        <div className="add-category">
            <button>Add Advertisement</button>        
            <CategoriesList />
        </div>
    )
  }
}
