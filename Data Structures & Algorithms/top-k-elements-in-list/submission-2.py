class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            dic[n] += 1
    
            ans = list(dic)
        ans.sort(key=lambda x: dic[x], reverse=True)
        return ans[:k]