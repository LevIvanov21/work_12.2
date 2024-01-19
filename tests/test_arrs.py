import pytest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


@pytest.mark.parametrize("coll, start, end, expected_result", [([1, 2, 3, 4], 1, 3, [2, 3]),
                                                               ([1, 2, 3] , 1, None, [2, 3]),
                                                               ([], 1, None, []),
                                                               ([1, 2, 3, 4, 5], None, -2, [1, 2, 3])])
def test_slice(coll, start, end, expected_result):
    assert arrs.my_slice(coll, start, end) == expected_result