# 215. Kth Largest Element in an Array

def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]
