methods {
    function _mint(address to, uint256 value) external envfree;
    function getBalance(address) external  returns (uint256) envfree;
}

rule checkMint() {
    address alice = address(0x034);
    address bob = address(123);
    address sadik = address(456);

    uint256 value1 = 1000000000000000000; // 1e18
    uint256 value2 = 2000000000000000000; // 2e18
    uint256 value3 = 3000000000000000000; // 3e18

    uint256 totalSupplyBefore = totalSupply();
    uint256 balanceOfaliceBefore = getBalance(alice);
    uint256 balanceOfbobBefore = getBalance(bob);
    uint256 balanceOfsadikBefore = getBalance(sadik);

    // call mint 3 times
    mathint actual = _mint(alice, value1);
    mathint actual = _mint(bob, value2);
    mathint actual = _mint(sadik, value3);

    uint256 totalSupplyAfter = totalSupply();
    uint256 balanceOfaliceAfter = getBalance(alice);
    uint256 balanceOfbobAfter = getBalance(bob);
    uint256 balanceOfsadikAfter = getBalance(sadik);

    assert totalSupplyBefore == (balanceOfaliceBefore + balanceOfbobBefore + balanceOfsadikBefore) <=> totalSupplyAfter == (value1 + value2 + value3);
    assert totalSupplyBefore < totalSupplyAfter <=> totalSupplyAfter > totalSupplyBefore;
    assert balanceOfaliceAfter > balanceOfaliceBefore <=> balanceOfaliceBefore < balanceOfaliceBefore;
    assert balanceOfbobAfter > balanceOfbobBefore <=> balanceOfbobBefore < balanceOfbobAfter;
    assert balanceOfsadikAfter > balanceOfsadikBefore <=> balanceOfsadikBefore < balanceOfsadikAfter;
}
