import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.arrays.valid_palindrome import isPalindrome


def test_isPalindrome():
    # Test case 1: Basic palindrome with spaces and punctuation
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    
    # Test case 2: Non-palindrome with spaces and punctuation
    assert isPalindrome("race a car") == False
    
    # Test case 3: Empty string
    assert isPalindrome(" ") == True

    # Test case 4: Single character and a number
    assert isPalindrome(" 0P") == False

if __name__ == "__main__":
    test_isPalindrome()
    print("All tests passed!")