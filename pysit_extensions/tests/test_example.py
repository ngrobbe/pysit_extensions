import pytest


def test_thing1():

    assert True

    with pytest.raises(Exception):
        raise Exception()
