# 7. Reverse Integer


def reverse(self, x: int) -> int:
    is_negative = x < 0

    x = abs(x)
    reverse_num = 0

    while x > 0:
        reverse_num = reverse_num * 10 + x % 10
        x //= 10

    if reverse_num > pow(2, 31):
        return 0
    return -reverse_num if is_negative else reverse_num
