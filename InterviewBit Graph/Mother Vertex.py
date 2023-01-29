import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def addedges(self, u, v, adj):
        adj[u - 1].append(v - 1)

    def DFS(self, v, visited, adj):
        visited[v] = True
        for i in adj[v]:
            if visited[i] == False:
                self.DFS(i, visited, adj)

    def motherVertex(self, A, B):
        adj = [[] for j in range(A)]
        for (x, y) in B:
            self.addedges(x, y, adj)
        visited = [False] * A
        v = 0
        for i in range(A):
            if visited[i] == False:
                self.DFS(i, visited, adj)
                v = i
        visited = [False] * A
        self.DFS(v, visited, adj)
        if any(i == False for i in visited):
            return 0
        else:
            return 1







