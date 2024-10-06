"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pointer1, pointer2, m1, m2 = 0, 0, 0, 0
        for i in range(0, (len(nums1) + len(nums2)) // 2 + 1):
            m2 = m1
            if pointer1 < len(nums1) and pointer2 < len(nums2):
                if nums1[pointer1] < nums2[pointer2]:
                    m1 = nums1[pointer1]
                    pointer1 += 1
                else:
                    m1 = nums2[pointer2]
                    pointer2 += 1
            else:
                if pointer1 == len(nums1):
                    m1 = nums2[pointer2]
                    pointer2 += 1
                else:
                    m1 = nums1[pointer1]
                    pointer1 += 1
        if (len(nums1) + len(nums2)) % 2 != 0:
            return m1
        else:
            return (m1 + m2) / 2
