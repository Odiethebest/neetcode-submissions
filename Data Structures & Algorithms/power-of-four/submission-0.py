class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            if n & (n - 1) == 0:
                if n % 3 == 1:
                    return True
        return False

