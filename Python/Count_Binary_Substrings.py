# 696. Count Binary Substrings

def countBinarySubstrings(self, s: str) -> int:
    current_count = 1
    previous_count = 0
    ans = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            ans += min(current_count, previous_count)
            previous_count = current_count
            current_count = 1

    return ans + min(current_count, previous_count)
