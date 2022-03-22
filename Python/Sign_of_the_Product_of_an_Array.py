# 1822. Sign of the Product of an Array


def arraySign(self, nums: List[int]) -> int:
    product = 1
    for num in nums:
        product *= num

    if product > 0:
        return 1
    elif product == 0:
        return 0
    else:
        return -1
