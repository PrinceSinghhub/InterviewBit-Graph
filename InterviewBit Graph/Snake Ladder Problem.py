class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def snakeLadder(self, A, B):
        sl = {}
        for u, v in A:
            sl[u] = v

        for u, v in B:
            sl[u] = v

        moves = [1, 2, 3, 4, 5, 6]
        visited = set()
        q = []
        q.append((1, 0))
        visited.add(1)

        while (len(q) > 0):
            pos, steps = q.pop(0)

            if (pos == 100):
                return steps

            for i in moves:
                new_pos = pos + i

                if (new_pos in sl):
                    new_pos = sl[new_pos]

                if (new_pos not in visited and new_pos <= 100):
                    q.append((new_pos, steps + 1))
                    visited.add(new_pos)

        return -1
