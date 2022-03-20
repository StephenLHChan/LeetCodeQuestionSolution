# 137. Single Number II


def singleNumber(self, nums: List[int]) -> int:
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    for num, count in nums_dict.items():
        if count == 1:
            return num
