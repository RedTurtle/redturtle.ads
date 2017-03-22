import React, { Component, PropTypes } from 'react';

class Command extends Component {
  render() {
    const { onClick } = this.props;
    return (
      <button type="submit"
              className="btn btn-default"
              onClick={onClick}>
        <span className="glyphicon glyphicon-search" aria-hidden="true"></span>
      </button>
    );
  }
}

Command.propTypes = {
  onClick: PropTypes.func.isRequired,
};

export default Command;
