methods {
    function min(uint256, uint256) external returns (uint256) envfree;
}

rule checkMin() {
    uint256 x;
    uint256 y;

    mathint expectedMin;

    if (y <= x) {
        expectedMin = y;
    } else {
        expectedMin = x;
    }

    mathint resultMin = min@withrevert(x, y);
    assert !lastReverted;

    assert resultMin == expectedMin;
}


// result link: https://prover.certora.com/output/3072084/9cf1a354ab5143d9a06568a9b3a6cdb7?
