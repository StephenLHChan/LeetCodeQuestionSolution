# 1523. Count Odd Numbers in an Interval Range

def countOdds(self, low: int, high: int) -> int:
    if (low % 2 == 1) or (high % 2 == 1):
        return (high - low) // 2 + 1
    return (high - low) // 2
