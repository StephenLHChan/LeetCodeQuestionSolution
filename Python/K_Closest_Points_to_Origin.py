# 973. K Closest Points to Origin

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda x: math.sqrt(x[0] * x[0] + x[1] * x[1]))

    return points[:k]
