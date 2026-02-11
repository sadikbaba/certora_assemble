// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract zerofloorSub {
    // source link: https://github.com/Vectorized/solady/blob/dcdfab80f4e6cb9ac35c91610b2a2ec42689ec79/src/utils/FixedPointMathLib.sol#L657
    // @dev notice i made the function external

    function zeroFloorSub(uint256 x, uint256 y) external pure returns (uint256 z) {
        // @solidity memory-safe-assembly
        assembly {
            z := mul(gt(x, y), sub(x, y))
        }
    }
}
