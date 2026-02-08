methods {
    function count() external returns (uint256) envfree;
    function increment() external envfree;
}

rule checkCounter() {
    // Pre-Call State
 //   require count() == 0;
    uint256 precallCount = count();

    // Method Call
    increment();
    increment();
    increment();

    // Post-call state
    uint256 postcallCount = count();
    // Assert that the post-call count is exactly one more than the pre-call count
    assert precallCount == 0;
    assert postcallCount == precallCount + 3;
}
