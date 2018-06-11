import React, { Component, PropTypes } from 'react';

class Advertisement extends Component {
  render() {
    const { data } = this.props;
    let title;
    let description;
    let price;
    let image;
    let category;
    let date;

    if (data.date) {
      date= <div className="adv-date">{data.date}</div>;
    }

    if (data.title) {
      title = <div className="adv-title"><a href={data.url}>{data.title}</a></div>;
    }

    if (data.category) {
      category = <span className="adv-category"><a href={data.category.url}>{data.category.title}</a></span>;
    }

    if (data.description) {
      description = <div className="adv-description">{data.description}</div>;
    }

    if (data.price) {
      price = <span className="adv-price">{data.price}</span>;
    }

    if (data.image_src) {
      image = <a href={data.url} title={data.title}>
          <figure><img src={data.image_src} alt={data.title}/></figure>
        </a>;
    }
    else{
        image = <span className="adv-nophoto"></span>
    }

    return (
      <div className="row">
        <div className="col-xs-3 col-sm-3 advertisement-image">
          {image}
        </div>
        <div className="col-xs-9 col-sm-9 advertisement-infos">
          {title}
          {description}
          {date}
          <div class="adv-details">
            {price}
            {category}
          </div>
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
