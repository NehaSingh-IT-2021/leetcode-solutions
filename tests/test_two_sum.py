import pytest
from src.arrays.two_sum import two_sum
from src.utils.test_utils import assert_equal

def test_two_sum():
    assert_equal(two_sum([2, 7, 11, 15], 9), [0, 1])
    assert_equal(two_sum([3, 2, 4], 6), [1, 2])
    assert_equal(two_sum([3, 3], 6), [0, 1])
    assert_equal(two_sum([1, 5, 3, 7], 10), [1, 3])
    assert_equal(two_sum([1, 2, 3, 4, 5], 7), [1, 4])

if __name__ == "__main__":
    pytest.main()