class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        n = len(students)
        res = n
        for s in sandwiches:
            cnt = 0
            while cnt < len(q) and q[0] != s:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if q[0] == s:
                q.popleft()
                res -= 1
            else:
                break
        return res