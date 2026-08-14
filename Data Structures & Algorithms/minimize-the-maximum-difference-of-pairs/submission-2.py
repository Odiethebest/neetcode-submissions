class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        n = len(nums)
        nums.sort()
        
        def count_pairs(diff):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count

        low = 0
        high = nums[-1] - nums[0]
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_pairs(mid) >= p:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans