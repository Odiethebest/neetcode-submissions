class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse = s[::-1]
        combined = s + '#' + reverse
        prefix = [0] * len(combined)
        for i in range(1, len(combined)):
            j = prefix[i-1]
            while j and combined[i] != combined[j]: j = prefix[j-1]
            if combined[i] == combined[j]: j += 1
            prefix[i] = j
        return reverse[:len(s)-prefix[-1]] + s
