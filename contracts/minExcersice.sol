// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Min {
    // source https://github.com/Vectorized/solady/blob/dcdfab80f4e6cb9ac35c91610b2a2ec42689ec79/src/utils/FixedPointMathLib.sol#L1100
    // i make it external for simplicity
    function min(uint256 x, uint256 y) external pure returns (uint256 z) {
        assembly {
            z := xor(x, mul(xor(x, y), lt(y, x)))
        }
        // @sadik comment standard solidity. if (y < x) { return y; } else { return x; }
    }
}
