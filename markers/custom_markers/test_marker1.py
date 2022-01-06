# to run with multiple markers, use pytest -m "USER and SMOKE" -v
import pytest


@pytest.mark.USER
@pytest.mark.REGRESSION
def test_adduser():
    assert True


@pytest.mark.USER
@pytest.mark.REGRESSION
def test_paymentmode():
    assert False


@pytest.mark.USER
@pytest.mark.SANITY
def test_selectplan():
    assert True


@pytest.mark.USER
@pytest.mark.SMOKE
def test_userverification():
    assert True

