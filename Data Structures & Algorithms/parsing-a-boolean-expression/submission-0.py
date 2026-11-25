class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c == ",":
                continue
            if c != ')':
                stk.append(c)
                continue
            yes = no = False
            while stk[-1] != "(":
                v = stk.pop()
                yes |= v == 't'
                no |= v == 'f'
            stk.pop()
            op = stk.pop()
            value = not yes if op == "!" else(not no if op == "&" else yes)
            stk.append("t" if value else "f")
        return stk[0] == "t"

    