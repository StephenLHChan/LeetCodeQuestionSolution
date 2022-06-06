# 2248. Intersection of Multiple Arrays

def intersection(self, nums: List[List[int]]) -> List[int]:
    seen = dict()
    for numArray in nums:
        for num in numArray:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
    result = []
    for (key, value) in seen.items():
        if value == len(nums):
            result.append(key)
    return sorted(result)
