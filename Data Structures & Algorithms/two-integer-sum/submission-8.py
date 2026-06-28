class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = defaultdict()
        for i, n in enumerate(nums):
            comp = target - n
            if comp in mySet:
                    return [mySet[comp],i]
            mySet[n] = i
        #return -1