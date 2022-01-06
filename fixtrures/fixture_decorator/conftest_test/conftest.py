import pytest


@pytest.fixture
def numbers():
    a = 3
    b = 6
    return a, b