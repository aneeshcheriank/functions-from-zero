import pytest

from hello import add

add_test_data = [(1, 1, 2), (-1, -1, -2), (-1, 4, 3)]


@pytest.mark.parametrize("a, b, expected", add_test_data)
def test_add(a, b, expected):
    assert expected == add(a, b)
