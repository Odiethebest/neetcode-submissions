class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        fac = 2
        while fac * fac <= n:
            while n % fac == 0:
                ans += fac
                n //= fac
            fac += 1
        return ans + (n if n > 1 else 0)
