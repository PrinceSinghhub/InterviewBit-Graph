class Solution:
    # @param A : list of list of integers
    # @return an integer

    def solve(self, A):
        ans = 0

        m = len(A)
        n = len(A[0])

        setA = set()
        setB = set()

        queueA = []
        queueB = []

        for i in range(m):
            queueA.append((i, 0))
            setA.add((i, 0))
            queueB.append((i, n - 1))
            setB.add((i, n - 1))

        for j in range(n):
            queueA.append((0, j))
            setA.add((0, j))
            queueB.append((m - 1, j))
            setB.add((m - 1, j))

        def bfs(Queue, Set):
            while Queue:
                x, y = Queue.pop(0)

                if (x > 0 and (x - 1, y) not in Set and A[x][y] <= A[x - 1][y]):
                    Queue.append((x - 1, y))
                    Set.add((x - 1, y))

                if (y > 0 and (x, y - 1) not in Set and A[x][y] <= A[x][y - 1]):
                    Queue.append((x, y - 1))
                    Set.add((x, y - 1))

                if (x + 1 < m and (x + 1, y) not in Set and A[x][y] <= A[x + 1][y]):
                    Queue.append((x + 1, y))
                    Set.add((x + 1, y))

                if (y + 1 < n and (x, y + 1) not in Set and A[x][y] <= A[x][y + 1]):
                    Queue.append((x, y + 1))
                    Set.add((x, y + 1))

        bfs(queueA, setA)
        bfs(queueB, setB)

        for a in setA:
            if a in setB:
                ans += 1

        return ans








