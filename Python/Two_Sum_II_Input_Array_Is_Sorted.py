# 167. Two Sum II - Input Array Is Sorted

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    seen = {}
    for index, number in enumerate(numbers):
        if (target - number) in seen:
            return [seen[target - number] + 1, index + 1]
        seen[number] = index
