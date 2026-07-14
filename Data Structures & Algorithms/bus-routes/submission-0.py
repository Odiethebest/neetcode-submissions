class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        n = len(routes)
        adjList = [[] for _ in range(n)]
        stopToRoutes = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].append(bus)
        
        if target not in stopToRoutes or source not in stopToRoutes:
            return -1
        
        for buses in stopToRoutes.values():
            for i in range(len(buses)):
                for j in range(i + 1, len(buses)):
                    u, v = buses[i], buses[j]
                    adjList[u].append(v)
                    adjList[v].append(u)
        
        q = deque(stopToRoutes[source])
        visited = set(stopToRoutes[source])
        target_buses = set(stopToRoutes[target])
        res = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in target_buses:
                    return res
                for nxtBus in adjList[node]:
                    if nxtBus not in visited:
                        visited.add(nxtBus)
                        q.append(nxtBus)
            res += 1
        return -1