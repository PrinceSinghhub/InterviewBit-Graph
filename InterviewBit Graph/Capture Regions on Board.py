from collections import deque


class Solution:

    def solve(self, A):
        row_count = len(A)

        col_count = len(A[0])

        for i in range(row_count):
            if A[i][0] == 'O':
                self.mark_boundary_connected(i, 0, A)

            if A[i][col_count - 1] == 'O':
                self.mark_boundary_connected(i, col_count - 1, A)

        for j in range(col_count):
            if A[0][j] == 'O':
                self.mark_boundary_connected(0, j, A)

            if A[row_count - 1][j] == 'O':
                self.mark_boundary_connected(row_count - 1, j, A)

        for i in range(row_count):
            for j in range(col_count):
                if A[i][j] == 'B':
                    A[i][j] = 'O'
                else:
                    A[i][j] = 'X'
        return A

    def mark_boundary_connected(self, boundary_i, boundary_j, board):
        q = deque()
        row_count = len(board)
        col_count = len(board[0])
        q.append([boundary_i, boundary_j])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while len(q) > 0:
            mark = q.popleft()

            board[mark[0]][mark[1]] = 'B'
            for i in range(4):
                x, y = mark[0] + dx[i], mark[1] + dy[i]

                if x < 0 or x >= row_count or y < 0 or y >= col_count:
                    continue

                if board[x][y] == 'O':
                    q.append([x, y])

                    board[x][y] = 'B'

