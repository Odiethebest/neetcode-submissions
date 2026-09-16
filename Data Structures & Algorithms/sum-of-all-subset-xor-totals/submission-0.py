class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for mask in range(1 << n):
            xorr = 0
            for i in range(n):
                if mask & (1 << i):
                    xorr ^= nums[i]
            res += xorr
        return res