class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                res.append(s[i])
            else:
                if not res:
                    return False
                if mapping[s[i]] == res[-1]:
                    res.pop()
                else:
                    return False
        return not res