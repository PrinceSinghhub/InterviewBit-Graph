class Solution:
    # @param A : list of list of integers
    # @return an integer
    def bfs(self, A, i, j, v):
        q = [(i, j)]
        res = 1
        while q:
            curr = q.pop(0)
            i = curr[0]
            j = curr[1]
            if i > 0:
                if A[i - 1][j] and not v[i - 1][j]:
                    q.append((i - 1, j))
                    v[i - 1][j] = 1
                    res += 1
                if j < len(A[0]) - 1 and A[i - 1][j + 1] and not v[i - 1][j + 1]:
                    q.append((i - 1, j + 1))
                    v[i - 1][j + 1] = 1
                    res += 1
                if j > 0 and A[i - 1][j - 1] and not v[i - 1][j - 1]:
                    q.append((i - 1, j - 1))
                    v[i - 1][j - 1] = 1
                    res += 1
            if i < len(A) - 1:
                if A[i + 1][j] and not v[i + 1][j]:
                    q.append((i + 1, j))
                    v[i + 1][j] = 1
                    res += 1
                if j < len(A[0]) - 1 and A[i + 1][j + 1] and not v[i + 1][j + 1]:
                    q.append((i + 1, j + 1))
                    v[i + 1][j + 1] = 1
                    res += 1
                if j > 0 and A[i + 1][j - 1] and not v[i + 1][j - 1]:
                    q.append((i + 1, j - 1))
                    v[i + 1][j - 1] = 1
                    res += 1
            if j > 0:
                if A[i][j - 1] and not v[i][j - 1]:
                    q.append((i, j - 1))
                    v[i][j - 1] = 1
                    res += 1
            if j < len(A[0]) - 1:
                if A[i][j + 1] and not v[i][j + 1]:
                    q.append((i, j + 1))
                    v[i][j + 1] = 1
                    res += 1
        return res

    def solve(self, A):
        res = 0
        v = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] and not v[i][j]:
                    v[i][j] = 1
                    length = self.bfs(A, i, j, v)
                    res = max(res, length)
        return res
