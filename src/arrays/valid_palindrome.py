import re

def isPalindrome( s: str) -> bool:
    s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if (len(s2) <=1 ):
        return True
    for i in range (len(s2)-1):
        if ((s2[i]) != (s2[len(s2)-1-i])):
            return False
    return True

result = isPalindrome("0P")
print(result)