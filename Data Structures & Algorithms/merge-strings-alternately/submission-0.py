class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        res = []
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[n:])
        res.append(word2[n:])
        return "".join(res)