# 1. Two Sum


def twoSum(self, nums: List[int], target: int) -> List[int]:
    two_sum_dict = dict()

    for i in range(0, len(nums)):
        if (target - nums[i]) in two_sum_dict:
            return [i, two_sum_dict.get(target - nums[i])]
        two_sum_dict[nums[i]] = i

    return []
