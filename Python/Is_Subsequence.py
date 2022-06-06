# 392. Is Subsequence

def isSubsequence(self, s: str, t: str) -> bool:
    count = 0
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    for i in range(0, len(t)):
        if count == len(s):
            return True
        if s[count] == t[i]:
            count += 1
    return count == len(s)
