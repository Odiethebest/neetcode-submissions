class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            cnt[num] += 1
            if maxCount < cnt[num]:
                res = num
                maxCount = cnt[num]
        return res