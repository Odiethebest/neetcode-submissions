class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        i = j = 0
        m1 = m2 = 0

        for cnt in range((l1 + l2) // 2 + 1):
            m2 = m1
            if i < l1 and j < l2:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < l1:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        if (l1 + l2) % 2 == 1:
            return float(m1)
        else:
            return (m1 + m2) / 2.0






