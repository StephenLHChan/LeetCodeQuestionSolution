#   202. Happy Number

def isHappy(self, n: int) -> bool:
    seen = set()
    return self.__isHappy(n, seen)


def __isHappy(self, n: int, seen: set) -> bool:
    if n == 1:
        return True
    if n in seen:
        return False

    seen.add(n)

    next = 0
    while n != 0:
        next += (n % 10) * (n % 10)
        n //= 10

    return self.__isHappy(next, seen)
