methods {
    function _mint(address to, uint256 value) external envfree;
    function getBalance(address) external returns (uint256) envfree;

    function _totalSupply() external returns (uint) envfree;
}

rule checkMint() {
    address alice;
    address bob;
    address sadik;

    require alice != bob;
    require alice != sadik;
    require bob != sadik;

    uint256 value1 = 1000000000000000000; // 1e18
    uint256 value2 = 2000000000000000000; // 2e18
    uint256 value3 = 3000000000000000000; // 3e18

    uint256 totalSupplyBefore = _totalSupply();
    uint256 balanceOfaliceBefore = getBalance(alice);
    uint256 balanceOfbobBefore = getBalance(bob);
    uint256 balanceOfsadikBefore = getBalance(sadik);

    // call mint 3 times
    _mint(alice, value1);
    _mint(bob, value2);
    _mint(sadik, value3);

    uint256 totalSupplyAfter = _totalSupply();
    uint256 balanceOfaliceAfter = getBalance(alice);
    uint256 balanceOfbobAfter = getBalance(bob);
    uint256 balanceOfsadikAfter = getBalance(sadik);

    // biConditional   <=>

    assert totalSupplyAfter == (totalSupplyBefore + value1 + value2 + value3);
    assert totalSupplyBefore < totalSupplyAfter <=> totalSupplyAfter > totalSupplyBefore;
    assert balanceOfaliceAfter == balanceOfaliceBefore + value1;
    assert balanceOfbobAfter == (balanceOfbobBefore + value2) <=> balanceOfbobBefore < balanceOfbobAfter;
    assert balanceOfsadikAfter == (balanceOfsadikBefore + value3) <=> balanceOfsadikBefore < balanceOfsadikAfter;
}
