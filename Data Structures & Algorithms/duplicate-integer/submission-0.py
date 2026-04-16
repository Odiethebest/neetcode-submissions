class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            dic[num] = 1
        return False
            
