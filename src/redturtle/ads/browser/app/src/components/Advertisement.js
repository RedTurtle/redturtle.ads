import React, { Component, PropTypes } from 'react';

class Advertisement extends Component {
  render() {
    const { data } = this.props;
    let title;
    let description;
    let price;
    let image;
    let category;

    if (data.title) {
      title = <div className="adv-title"><a href={data.url}>{data.title}</a></div>;
    }

    if (data.category) {
      category = <div className="adv-category"><a href={data.category.url}>{data.category.title}</a></div>;
    }

    if (data.description) {
      description = <div className="adv-description">{data.description}</div>;
    }

    if (data.price) {
      price = <div className="adv-price">{data.price}</div>;
    }

    if (data.image_src) {
      image = <a href={data.url} title={data.title}>
          <figure><img src={data.image_src} alt={data.title}/></figure>
        </a>;
    }

    return (
      <div className="row">
        <div className="col-xs-3 col-sm-3 advertisement-image">
          {image}
        </div>
        <div className="col-xs-9 col-sm-9 advertisement-infos">
          {title}
          {description}
          {category}
          {price}
        </div>
      </div>
    );
  }
}

Advertisement.propTypes = {
  data: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string, //mi arrivano sia dei numeri che delle stringhe
    price: PropTypes.string,
  }).isRequired,
};

export default Advertisement;
