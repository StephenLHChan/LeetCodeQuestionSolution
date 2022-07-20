# 983. Minimum Cost For Tickets

def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    minCosts = [0] * (days[-1] + 1)
    days = set(days)
    for i in range(1, len(minCosts)):
        if i in days:
            minCosts[i] = min(minCosts[max(i - 1, 0)] + costs[0], minCosts[max(
                i - 7, 0)] + costs[1], minCosts[max(i - 30, 0)] + costs[2])
        else:
            minCosts[i] = minCosts[i - 1]
    return minCosts[-1]
