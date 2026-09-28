class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        best = [(None, float("-inf"))] * 3
        for xi, yi in zip(x, y):
            for i, (xj, yj) in enumerate(best):
                if xi == xj:
                    if yi > yj:
                        best[i] = (xi, yi)
                        best.sort(key=lambda t: t[1], reverse=True)
                    break
            else:
                if yi > best[0][1]:
                    best = [(xi, yi), best[0], best[1]]
                elif yi > best[1][1]:
                    best = [best[0], (xi, yi), best[1]]
                elif yi > best[2][1]:
                    best[2] = (xi, yi)

        return sum(v for _, v in best) if best[2][1] > float("-inf") else -1