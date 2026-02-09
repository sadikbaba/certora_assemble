// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// uniswap link: https://github.com/Uniswap/v2-core/blob/ee547b17853e71ed4e0101ccfd52e70d5acded58/contracts/UniswapV2ERC20.sol#L40-L44

contract UniswapV2Mint {
    event Transfer(address indexed from, address indexed to, uint256 value);

    uint256 totalSupply;
    mapping(address => uint256) balanceOf;

    // For simplicity, I changed the function visibility from internal to external.
    // I am aware that making the function external removes its protection.
    // This change is for educational purposes only,
    // as I only want to test the math inside the function.

    function _mint(address to, uint256 value) external {
        totalSupply = totalSupply +(value);
        balanceOf[to] = balanceOf[to] + (value);
        emit Transfer(address(0), to, value);
    }

    // to check balance of user 

    function getBalance(address user) external view returns (uint256) {
    return balanceOf[user];
    }
}

