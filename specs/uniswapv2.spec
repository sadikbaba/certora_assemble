methods {
    function totalSupply() external returns (uint256) envfree;
}

rule totalSupplyWillNotChange(env e, method f, calldataarg args) filtered { f -> !f.isView } // target only function that are not view
{
    mathint totalSupplyBefore = totalSupply(e);

    f(e, args);

    mathint totalSupplyAfter = totalSupply(e);

    if (f.selector == sig:approve(address, uint).selector) {
        assert totalSupplyAfter == totalSupplyBefore + 0; 
        // i did this for demonstration, example total supply acn only,
        // increase or decrease when burn or mint, that is why we use if suppose uniswapv2 have external mint function
        // we will do 
        //if(f.selector == sig:mint(address, uint).selector) {
        // asserttotalSupplyAfter => totalSupplyBefore }
    } else {
        assert totalSupplyAfter == totalSupplyBefore;
    }
}
