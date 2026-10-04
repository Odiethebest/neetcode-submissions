class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cntK = nums.count(k)
        max_gain = 0

        for num in range(1, 51):
            if num == k: continue
            current_gain = 0
            for x in nums:
                if x == num:
                    current_gain += 1
                elif x == k:
                    current_gain -= 1
                if current_gain < 0:
                    current_gain = 0
                max_gain = max(max_gain, current_gain)

        return cntK + max_gain