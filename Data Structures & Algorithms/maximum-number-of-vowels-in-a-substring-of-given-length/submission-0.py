class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = ans = 0
        for i, c in enumerate(s):
            cnt += c in 'aeiou'
            if i >= k: cnt -= s[i - k] in 'aeiou'
            if i >= k - 1: ans = max(ans, cnt)
        return ans
