class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i, j)]
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    res = True
            
            if not res and j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    res = True
            
            memo[(i, j)] = res
            return res
        return dfs(0, 0, 0)