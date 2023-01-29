import heapq


class Solution:
    def dijikstra(self, d, adj, start):
        heap = []
        heapq.heappush(heap, (0, start))
        d[start] = 0

        while heap:
            cur = heapq.heappop(heap)[1]

            for it in adj[cur]:
                if d[it[0]] > d[cur] + it[1]:
                    d[it[0]] = d[cur] + it[1]
                    heapq.heappush(heap, (d[it[0]], it[0]))

    def solve(self, A, B, C, D, E):
        adj = [[] for _ in range(A + 1)]
        for i in range(len(B)):
            adj[B[i][0]].append((B[i][1], B[i][2]))
            adj[B[i][1]].append((B[i][0], B[i][2]))

        ds = [10000000 for _ in range(A + 2)]
        de = [10000000 for _ in range(A + 2)]

        self.dijikstra(ds, adj, C)
        self.dijikstra(de, adj, D)

        ans = ds[D]
        for i in range(len(E)):
            dist = ds[E[i][0]] + de[E[i][1]] + E[i][2]
            dist1 = ds[E[i][1]] + de[E[i][0]] + E[i][2]
            ans = min(ans, dist, dist1)

        if ans != 10000000:
            return ans
        return -1

