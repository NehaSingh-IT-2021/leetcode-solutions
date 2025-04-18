import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.arrays.two_sum import two_sum

def test_two_sum():
    # Test case 1: Basic case
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: No solution
    assert two_sum([1, 2, 3], 7) == []
    
    # Test case 3: Multiple possible answers but return first
    assert two_sum([3, 3], 6) == [0, 1]

if __name__ == "__main__":
    test_two_sum()
    print("All tests passed!")