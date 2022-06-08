# 1331. Rank Transform of an Array

def arrayRankTransform(self, arr: List[int]) -> List[int]:
    ranks = {}
    for rank, num in enumerate(sorted(set(arr))):
        ranks[num] = rank+1
    return [ranks[num] for num in arr]
