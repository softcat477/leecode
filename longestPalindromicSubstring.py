from typing import Tuple
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s, left_idx, right_idx) -> Tuple[bool, str]:

            while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                left_idx, right_idx = left_idx - 1, right_idx + 1

            return s[left_idx + 1 : right_idx - 1 + 1]

        if len(s) == 1:
            return s
        # Iterate through the arrayy
        ret_str = ""
        for i in range(len(s)):
            # The palindrom has an odd length, the centered char is i
            odd_p = isPalindrome(s, i, i)

            # The palindrom has an even length, the centered char is i and i+1
            even_p = ""
            if i+1 < len(s) and s[i+1] == s[i]:
                even_p = isPalindrome(s, i, i+1)
            ret_str = max(ret_str, odd_p, even_p, key = len)

        return ret_str

sol = Solution()

print (sol.longestPalindrome("babad"), "bab")
print (sol.longestPalindrome("cbbd"), "bb")
print (sol.longestPalindrome("AAabcdcbaBBcBaCat"), "abcdcba")
print (sol.longestPalindrome("abcdcbabc"), "abcdcba")
