# 33. Search in Rotated Sorted Array
def search(self, nums: List[int], target: int) -> int:
    def find_rotate_index(A):
        left = 0
        right = len(A) - 1
        if A[left] < A[right]:
            return 0

        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] > A[mid + 1]:
                return mid + 1
            if A[mid] < A[left]:
                right = mid - 1
            else:
                left = mid + 1

    def search(left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    rotate_index = find_rotate_index(nums)

    if nums[rotate_index] == target:
        return rotate_index
    if rotate_index == 0:
        return search(0, len(nums) - 1)
    if target < nums[0]:
        return search(rotate_index, len(nums) - 1)
    return search(0, rotate_index)
