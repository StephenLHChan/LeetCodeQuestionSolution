# 1570. Dot Product of Two Sparse Vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}

        for i, num in enumerate(nums):
            if num != 0:
                self.nums[i] = num

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        for key in self.nums:
            if key in vec.nums:
                result += self.nums[key] * vec.nums[key]
        return result
