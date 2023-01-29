import collections


class Solution:
    def solve(self, A, B, C):
        queue = collections.deque([])
        queue.append((0, 0, 0))
        completed = [[False for i in range(B)] for j in range(A)]
        while (len(queue) != 0):
            i, j, cost = queue.popleft()
            if (completed[i][j] == True):
                continue
            completed[i][j] = True
            if (i == A - 1 and j == B - 1):
                return cost
            if (j + 1 < B and not completed[i][j + 1]):

                if (C[i][j] == 'R'):
                    queue.appendleft((i, j + 1, cost))
                else:
                    queue.append((i, j + 1, cost + 1))

            if (i + 1 < A and not completed[i + 1][j]):

                if (C[i][j] == 'D'):
                    queue.appendleft((i + 1, j, cost))
                else:
                    queue.append((i + 1, j, cost + 1))

            if (j - 1 >= 0 and not completed[i][j - 1]):

                if (C[i][j] == 'L'):
                    queue.appendleft((i, j - 1, cost))
                else:
                    queue.append((i, j - 1, cost + 1))

            if (i - 1 >= 0 and not completed[i - 1][j]):

                if (C[i][j] == 'U'):
                    queue.appendleft((i - 1, j, cost))
                else:
                    queue.append((i - 1, j, cost + 1))


