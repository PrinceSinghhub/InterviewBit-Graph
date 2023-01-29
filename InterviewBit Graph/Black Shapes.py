class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        m, n = len(A), len(A[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):

            if (
                    i < 0 or i >= m or j < 0 or j >= n or  # out of bounds
                    A[i][j] == 'O' or  # useless char
                    visited[i][j]  # already visited
            ):
                return

            visited[i][j] = True

            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'X' and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count

