# 821. Shortest Distance to a Character

# not finished

def shortestToChar(self, s: str, c: str) -> List[int]:

    s_dict = {}  # char : index
    shortest_distance = []

    for i, char in enumerate(s):
        if char == c:
            shortest_distance.append(0)
        elif i == 0:
            shortest_distance.append(len(s))
        else:
            shortest_distance.append(shortest_distance[-1] + 1)

    for i in range(2, len(s) + 1):
        shortest_distance[-i] = min(shortest_distance[-i],
                                    shortest_distance[-i + 1] + 1)

    return shortest_distance
