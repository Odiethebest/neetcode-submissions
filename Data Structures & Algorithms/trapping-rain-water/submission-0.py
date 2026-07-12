class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stk = []
        res = 0

        for i in range(len(height)):
            while stk and height[i] >= height[stk[-1]]:
                mid = height[stk.pop()]
                if stk:
                    right = height[i]
                    left = height[stk[-1]]
                    h = min(right, left) - mid
                    w = i - stk[-1] - 1
                    res += h * w
            stk.append(i)
        return res