import pytest


@pytest.mark.SMOKE
def test_signup():
    a = 2
    b = 3
    assert a == b, "a and b are not equal"


@pytest.mark.REGRESSION
def test_login():
    a = 2
    b = 3
    assert a == b, "a and b are not equal"


@pytest.mark.SANITY
def test_predictscore():
    assert True


@pytest.mark.SMOKE
def test_winprize():
    assert False

