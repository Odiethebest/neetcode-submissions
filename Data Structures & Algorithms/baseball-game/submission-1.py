class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for s in operations:
            if s == '+':
                Sum = (res[-1] + res[-2])
                res.append(Sum)
            elif s == 'C':
                res.pop()
            elif s == 'D':
                Double = 2 * res[-1]
                res.append(Double)
            else:
                res.append(int(s))
        return sum(res)
