class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ''.join(ch for ch in s if ch.isalpha() or ch.isnumeric())
        return s2 == s2[::-1]
