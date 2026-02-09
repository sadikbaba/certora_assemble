methods {
    function add(uint256, uint256) external returns (uint256) envfree;
}

/** * Note on Solidity 0.8+ Overflows:
 * By default, Certora handles reverts by "pruning" the path. This means if a function 
 * reverts (like an overflow in 0.8), the Prover simply ignores that case rather 
 * than failing the rule.
 *
 * rule mathRevert() {
 * uint256 a; 
 * uint256 b = max_uint256;
 * uint256 c = add(a, b); // If a > 0, this reverts in Solidity 0.8
 * assert c == a + b;     // This rule PASSES because the Prover only checks 
 * // paths that don't revert.
 * }
 *
 * To change this behavior, use:
 * 1. functionName@withrevert(args): Tells the Prover NOT to prune the revert. 
 * You can then check `lastReverted` to see if the math failed.
 * 2. expect_revert: A wrapper used to prove that a function MUST revert.
 */

rule mathRevert() {
    uint256 a;
    uint256 b ;

    uint256 c = add@withrevert(a, b);

    assert (a + b>max_uint256) => lastReverted;
}
