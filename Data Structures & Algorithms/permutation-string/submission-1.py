class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = {}
        for c in s1:
            cnt1[c] = 1 + cnt1.get(c, 0)
        
        need = len(cnt1)
        for i in range(len(s2)):
            cnt2, cur = {}, 0
            for j in range(i, len(s2)):
                cnt2[s2[j]] = 1 + cnt2.get(s2[j],0)
                if cnt1.get(s2[j],0) < cnt2[s2[j]]:
                    break
                if cnt1.get(s2[j],0) == cnt2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False