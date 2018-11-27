import cx from 'classnames';
import { Component } from 'react';

export default class Counter extends Component {
  state = {
    count: 42
  };
  handleClick = () => {
    this.setState(({ count }) => ({
      count: count + 1
    }));
  };
  render() {
    return (
        <div>
        <h2 className="counter">{this.state.count}</h2>
    <button className="counter-button" onClick={this.handleClick}>
        Click
    </button>
    </div>);
  }
}