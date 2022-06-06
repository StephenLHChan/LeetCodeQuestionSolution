# 1930. Unique Length-3 Palindromic Subsequences

from operator import le


def countPalindromicSubsequence(self, s: str) -> int:
    res = 0
    unq_str = set(s)
    for ch in unq_str:
        left = s.find(ch)
        right = s.rfind(ch)

        if(right > left):
            res += len(set(s[left + 1: right]))

    return res
