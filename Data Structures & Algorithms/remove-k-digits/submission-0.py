class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for c in num:
            while k > 0 and stk and stk[-1] > c:
                k -= 1
                stk.pop()
            stk.append(c)
        
        while stk and k:
            stk.pop()
            k -= 1
        
        i = 0
        while i < len(stk) and stk[i] == '0':
            i += 1

        res = stk[i:]
        return ''.join(res) if res else "0"
        