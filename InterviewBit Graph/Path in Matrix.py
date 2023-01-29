class Solution:
    # @param A : list of list of integers
    # @return an integer
    def check(self, metrix, i, j):
        if metrix[i][j] == 0:
            return 0
        else:
            return 1

    def checkPath(self, A):
        n = len(A)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    start = [i, j]
        q = [start]
        visited[start[0]][start[1]] = 1
        while q:
            curr = q.pop(0)
            i = curr[0]
            j = curr[1]
            if A[i][j] == 2:
                return 1
            if i > 0:
                c = self.check(A, i - 1, j)
                if c and not visited[i - 1][j]:
                    q.append([i - 1, j])
                    visited[i - 1][j] = 1
            if i < n - 1:
                c = self.check(A, i + 1, j)
                if c and not visited[i + 1][j]:
                    q.append([i + 1, j])
                    visited[i + 1][j] = 1
            if j > 0:
                c = self.check(A, i, j - 1)
                if c and not visited[i][j - 1]:
                    q.append([i, j - 1])
                    visited[i][j - 1] = 1
            if j < n - 1:
                c = self.check(A, i, j + 1)
                if c and not visited[i][j + 1]:
                    q.append([i, j + 1])
                    visited[i][j + 1] = 1
        return 0

