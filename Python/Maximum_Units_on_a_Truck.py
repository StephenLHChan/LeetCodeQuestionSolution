# 1710. Maximum Units on a Truck

def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for box, num in boxTypes:
        boxes = min(box, truckSize)
        ans += boxes * num
        truckSize -= boxes
        if truckSize == 0:
            return ans
    return ans
