
pragma solidity >=0.5.0 <0.6.0;
pragma experimental ABIEncoderV2;

contract Ownable {
    address payable private _owner;
    address payable public constant incognitoAddress = 0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De;
    event OwnershipTransferred(
        address indexed previousOwner,
        address indexed newOwner
    );

    constructor() internal {
        _owner = msg.sender;
        emit OwnershipTransferred(address(0), _owner);
    }

    function owner() public view returns (address payable) {
        return _owner;
    }

    modifier onlyOwner() {
        require(isOwner());
        _;
    }

    function isOwner() public view returns (bool) {
        return msg.sender == _owner;
    }

    function renounceOwnership() public onlyOwner {
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }

    function transferOwnership(address payable newOwner) public onlyOwner {
        _transferOwnership(newOwner);
    }

    function _transferOwnership(address payable newOwner) internal {
        require(newOwner != address(0));
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
}

contract BookStoreInit is Ownable {

    struct order{
        uint256 token;
        uint timestamp;
        uint8 quantity;
        uint price_in_wei;
    }

    mapping(address => order[]) ownerToOrderList;

    function withdraw() internal {
        address payable _owner = owner();
        _owner.transfer(address(this).balance);
    }

    function SendToken(address _to, uint256 _token, uint _ether_amount, uint8 _quantity) internal {
        ownerToOrderList[_to].push(order(_token, now, _quantity, _ether_amount));
    }
}


contract BookStore is BookStoreInit{
    function implementTransaction(address payable _from, uint256 _token, uint8 _quantity) external payable {
        require(msg.sender == _from, "Invalid transaction");
        withdraw();
        SendToken(_from, _token, msg.value, _quantity);
    }
    function getOrderHistory(address _user) external view returns (order[] memory) {
        order[] memory result = new order[](ownerToOrderList[_user].length);
        result = ownerToOrderList[_user];
        return result;
    }

    function getBalance()  external view returns (uint256){
        return address(this).balance;
    }
}