class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt_map = Counter(tasks)
        maxHeap = [-cnt for cnt in cnt_map.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time