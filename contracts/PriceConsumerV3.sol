// SPDX-License-Identifier: MIT

pragma solidity >=0.6.2 <0.8.0;

import "./interfaces/AggregatorV3Interface.sol";

library SafeDiv {
    /**
     * @dev Returns the integer division of two signed integers. Reverts on
     * division by zero. The result is rounded towards zero.
     *
     * Counterpart to Solidity's `/` operator. Note: this function uses a
     * `revert` opcode (which leaves remaining gas untouched) while Solidity
     * uses an invalid opcode to revert (consuming all remaining gas).
     *
     * Requirements:
     *
     * - The divisor cannot be zero.
     */
    function div(int256 a, int256 b) internal pure returns (int256) {
        require(b > 0, "SafeMath: division by zero");
        int256 c = a / b;

        return c;
    }
}

contract PriceConsumerV3 {
    using SafeDiv for int256;

    AggregatorV3Interface internal priceFeedEth;
    AggregatorV3Interface internal priceFeedJPY;

    /**
     * Network: Rinkeby
     * Aggregator: ETH/USD
     * Address: 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
     */

    /**
     * Network: Rinkeby
     * Aggregator: JPY/USD
     * Address: 0x3Ae2F46a2D84e3D5590ee6Ee5116B80caF77DeCA
     */

    constructor() public {
        priceFeedEth = AggregatorV3Interface(address(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e));
        priceFeedJPY = AggregatorV3Interface(address(0x3Ae2F46a2D84e3D5590ee6Ee5116B80caF77DeCA));
    }

    /**
     * Returns the latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            uint80 roundID1, 
            int price1,
            uint startedAt1,
            uint timeStamp1,
            uint80 answeredInRound1
        ) = priceFeedEth.latestRoundData();

        (
            uint80 roundID2,
            int price2,
            uint startedAt2,
            uint timeStamp2,
            uint80 answeredInRound2
        ) = priceFeedJPY.latestRoundData();

        return price1.div(price2);
    }
}
