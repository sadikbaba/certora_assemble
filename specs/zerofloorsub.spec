methods {
    function zeroFloorSub(uint256, uint256) external returns (uint256) envfree;
}

rule checkzerofloorsub() {
    uint256 x;
    uint256 y;

    mathint expectedZeroFloorSub;

    if (x > y) {
        expectedZeroFloorSub =  (x - y);

    } else {
        expectedZeroFloorSub =  0;
    }

    mathint result = zeroFloorSub@withrevert(x,y);
     assert !lastReverted;

    assert result == expectedZeroFloorSub;
}

// result link : https://prover.certora.com/output/3072084/02afafcfa32241c4b6ac21584fe357ac