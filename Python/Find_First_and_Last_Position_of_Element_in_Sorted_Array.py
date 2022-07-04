# 34. Find First and Last Position of Element in Sorted Array

def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchLeftIndex(A, x):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchRightIndex(A, x):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    if target not in nums:
        return [-1, -1]
    if len(nums) == 0:
        return [-1, -1]

    return [searchLeftIndex(nums, target), searchRightIndex(nums, target)]
