import React, { Component, PropTypes } from 'react';

class Category extends Component {
  render() {
    const { data } = this.props;

    return (
      <div className="category">
          <figure>
              <a href={data.url}><img src={data.image} alt={data.title} /></a>
          </figure>
          <div className="category-title">
             <a href={data.url}>{data.title}</a>
          </div>
      </div>
    );
  }
}

Category.propTypes = {
  data: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired, 
    url: PropTypes.string.isRequired,
  }).isRequired,
};

export default Category;
