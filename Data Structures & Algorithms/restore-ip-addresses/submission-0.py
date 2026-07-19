class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def valid(num):
            return len(num) == 1 or (int(num) < 256 and num[0] != "0")

        def add(s1, s2, s3, s4):
            if s1 + s2 + s3 + s4 != len(s):
                return

            num1 = s[:s1]
            num2 = s[s1:s1+s2]
            num3 = s[s1+s2:s1+s2+s3]
            num4 = s[s1+s2+s3:]
            if valid(num1) and valid(num2) and valid(num3) and valid(num4):
                res.append(num1 + "." + num2 + "." + num3 + "." + num4)

        for seg1 in range(1, 4):
            for seg2 in range(1, 4):
                for seg3 in range(1, 4):
                    for seg4 in range(1, 4):
                        add(seg1, seg2, seg3, seg4)

        return res