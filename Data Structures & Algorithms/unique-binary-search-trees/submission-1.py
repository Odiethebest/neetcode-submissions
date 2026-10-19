class Solution:
    def numTrees(self, n: int) -> int:
        cnts = [0] * (n + 1)
        cnts[0] = 1
        for size in range(1, n + 1):
            for left in range(size): cnts[size] += cnts[left] * cnts[size - 1- left]
        return cnts[n]
