# 217. Contains Duplicate

def containsDuplicate(self, nums: List[int]) -> bool:
    numsSet = set(nums)
    return not len(numsSet) == len(nums)
