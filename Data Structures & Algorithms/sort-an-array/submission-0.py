class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def cnt_sort():
            cnt = defaultdict(int)
            minVal, maxVal = min(nums), max(nums)
            for num in nums:
                cnt[num] += 1
            
            idx = 0
            for num in range(minVal, maxVal + 1):
                while cnt[num] > 0:
                    nums[idx] = num
                    idx += 1
                    cnt[num] -= 1
        cnt_sort()
        return nums