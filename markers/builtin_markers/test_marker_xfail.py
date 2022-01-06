import pytest


@pytest.mark.xfail
def test_sum():
    a = 4
    b = 3
    assert a + b == 6, f"Expected: {a+b}, Actual:{6}"


@pytest.mark.xfail
def test_sub():
    a = 4
    b = 3
    assert a - b == 2, f"Expected: {a - b}, Actual:{2}"


@pytest.mark.xfail
def test_mul():
    a = 4
    b = 3
    assert a * b == 19, f"Expected: {a * b}, Actual:{19}"


def test_div():
    a = 4
    b = 3
    assert a // b == 2, f"Expected: {a // b}, Actual:{2}"

