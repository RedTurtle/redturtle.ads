import React, { Component } from 'react';
// import Command from '../components/Command';
// import CategoriesList from '../containers/CategoriesList';

// import Content from '../components/Content';

export default class AddNewAdvertisementContainer extends Component {

  render() {
    const apiUrl = document.body.getAttribute('data-portal-url');
    const url = apiUrl + '/@@create_adv'
    return (
        <div className="add-category">
            <a href="http://localhost:8080/mercatino/contact-info">Add Advertisement</a>
        </div>
    )
  }
}
