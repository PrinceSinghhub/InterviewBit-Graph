class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        dist = math.sqrt(5)
        import heapq
        def heuristic(x, y):
            return (((x - E) ** 2 + (y - F) ** 2) ** 0.5)

        heap = [(heuristic(C, D), 0, C, D)]
        seen = {(C, D): 0}
        while heap:
            _, steps, i, j = heapq.heappop(heap)
            if i == E and j == F:
                return steps
            for di, dj in (1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1):
                x, y = i + di, j + dj
                if 0 < x <= A and 0 < y <= B and ((x, y) not in seen or steps + 1 < seen[(x, y)]):
                    seen[(x, y)] = steps + 1
                    heapq.heappush(heap, (steps + 1 + heuristic(x, y), steps + 1, x, y))

        return -1
