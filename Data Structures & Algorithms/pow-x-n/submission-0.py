class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        res = 1.0
        cnt = 0
        while cnt < n:
            res = res * x
            cnt += 1
        return res