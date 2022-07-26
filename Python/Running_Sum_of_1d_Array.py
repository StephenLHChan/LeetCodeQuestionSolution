# 1480. Running Sum of 1d Array

def runningSum(self, nums: List[int]) -> List[int]:
    current_sum = 0
    res = []
    for num in nums:
        current_sum += num
        res.append(current_sum)
    return res
