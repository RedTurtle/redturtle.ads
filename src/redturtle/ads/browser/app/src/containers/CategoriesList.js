import React, { Component } from 'react';
import axios from 'axios';
import Category from '../components/Category';


export default class CategoriesList extends Component {

  constructor(props) {
    super(props);
    this.state = {categories: []};
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
  }
  render() {
    const theData = this.state.categories;
    let resRender = theData.map((category) => {
        return <Category key={category.id} data={category} />
    });
    
    if (theData){
        return (
        <div className="categories-list">
            {resRender}
        </div>
        );
   } else{
      return (
          <div className="categories-list">
              <p>No categories available</p>
          </div>
      )
   }
  }
}
