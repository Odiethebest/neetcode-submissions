class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        num = 0
        op = '+'
        s = s.replace(' ','')

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stk.append(num)
                elif op == '-':
                    stk.append(-num)
                elif op == '*':
                    stk.append(stk.pop() * num)
                else:
                    prev = stk.pop()
                    stk.append(int(prev / num))
                op = ch
                num = 0
        
        return sum(stk)