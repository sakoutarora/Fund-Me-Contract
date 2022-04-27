// SPDX License Identifier: MIT
pragma solidity 0.8.7;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    uint256 public totalFunds;
    mapping(address => uint256) public byAdd;
    address public owner;
    event Deposit(uint256);
    AggregatorV3Interface pricefeed;

    constructor(address _priceFeed) {
        pricefeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function Fund() external payable {
        uint256 currprice = (getprice() * msg.value) / (10**18);
        require(currprice >= 50 * (10**18), "SEND ATLEAST $50");
        emit Deposit(currprice);
        byAdd[msg.sender] += msg.value;
        totalFunds += msg.value;
    }

    function getEntry() external view returns (uint256) {
        uint256 basic = 50 * (10**18);
        uint256 price = getprice();
        uint256 precision = 1 * (10**18);
        return (basic * precision) / price;
    }

    function getprice() public view returns (uint256) {
        (, int256 price, , , ) = pricefeed.latestRoundData();
        return (uint256(price) * 10**10);
    }

    modifier OnlyOwner() {
        require(msg.sender == owner, "ONLY OWNER");
        _;
    }

    function withdraw() public OnlyOwner {
        (bool suc, ) = payable(owner).call{value: totalFunds}("");
        require(suc, "Transcation Failed");
        totalFunds = 0;
    }
}
