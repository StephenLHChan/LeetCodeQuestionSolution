# 976. Largest Perimeter Triangle


def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(1, len(nums) - 1):
        if nums[-i - 1] + nums[-i - 2] > nums[-i]:
            return nums[-i - 1] + nums[-i - 2] + nums[-i]

    return 0
