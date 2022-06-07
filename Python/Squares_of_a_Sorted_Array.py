# 977. Squares of a Sorted Array

def sortedSquares(self, nums: List[int]) -> List[int]:
    nums = list(map(lambda x: x * x, nums))
    return sorted(nums)
