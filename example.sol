// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract RestrictedVault {
    address public allowedSender;
    uint256 public totalDeposits;

    constructor(address _allowedSender) {
        allowedSender = _allowedSender;
    }

    // Developer tries to restrict who can send ETH
    receive() external payable {
        require(msg.sender == allowedSender, "Not allowed to send ETH");
        totalDeposits += msg.value;
    }

    fallback() external payable {
        require(msg.sender == allowedSender, "Not allowed to send ETH");
        totalDeposits += msg.value;
    }

    function withdraw(address payable to, uint256 amount) external {
        require(msg.sender == allowedSender, "Only controller");
        require(address(this).balance >= amount, "Insufficient balance");

        to.transfer(amount);
    }

    function vaultBalance() external view returns (uint256) {
        return address(this).balance;
    }
}