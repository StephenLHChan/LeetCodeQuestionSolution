# 88. Merge Sorted Array

# Solution 1
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for num in nums2:
        nums1[m] = num
        m += 1

    nums1.sort()


# Solution 2
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1

    for p in range(m + n - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
