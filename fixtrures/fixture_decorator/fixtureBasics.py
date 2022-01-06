import pytest


@pytest.fixture
def numbers():
    a = 3
    b = 6
    return a, b


def test_add(numbers):
    assert numbers[0] + numbers[1] == 8, f"expected:{numbers[0] + numbers[1]}, result: {8}"


