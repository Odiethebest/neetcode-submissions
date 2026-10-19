class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [0] * (len(matrix[0]) + 1)
        answer = 0
        for row in matrix:
            diagonal = 0
            for j, value in enumerate(row, 1):
                above = dp[j]
                dp[j] = 1 + min(above, dp[j - 1], diagonal) if value else 0
                answer += dp[j]
                diagonal = above
        return answer
