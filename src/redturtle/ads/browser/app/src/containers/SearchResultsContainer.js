import React, { Component } from 'react';
import { connect } from 'react-redux';
import Advertisement from '../components/Advertisement';
import ReactPaginate from 'react-paginate';
import { getSearchResults } from '../actions';

export class SearchResultsContainer extends Component {

  render() {

    const { getSearchResults } = this.props;

    const handlePageChange = (e) => getSearchResults(e.selected);

    const results = this.props.data.data; /* XXX ?? */
    const pagination = this.props.pagination;

    let resRender;
    let paginateRender;

    if (!results) {
      resRender = <p className="no-results">No advertisements found</p>;
    } else {
      resRender = results.map((result) => <Advertisement key={result.id} data={result} />);
      if (this.props.pagination && pagination.infos.totalPages > 1) {
        paginateRender = <ReactPaginate
          previousLabel={'previous'}
          nextLabel={'next'}
          breakLabel={<a href="">...</a>}
          breakClassName={'break-me'}
          pageCount={pagination.infos.totalPages}
          marginPagesDisplayed={2}
          pageRangeDisplayed={5}
          onPageChange={handlePageChange}
          containerClassName={'pagination'}
          subContainerClassName={'pages pagination'}
          activeClassName={'active'} />;
      }
    }

    return (
      <div className="results-container">
        {resRender}
        {paginateRender}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  data: state.data,
  pagination: state.pagination,
});

export default connect(mapStateToProps, { getSearchResults })(SearchResultsContainer);
