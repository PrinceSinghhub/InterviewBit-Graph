class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        return 1 if A > len(B) else 0

        visited = dict([(x, False) for x in range(1, A + 1)])
        prereq = dict((B[i], C[i]) for i in range(0, len(B)))

        node = self.getNonVisited(visited)

        while not node is None:
            visited[node] = True

            pre = prereq.get(node)

            print((node, pre))
            if not pre is None:
                node = pre
                if visited[node] == True:
                    return 0
            else:
                node = self.getNonVisited(visited)

        return 1

    def getNonVisited(self, visited):
        for v in visited:
            if visited[v] == False:
                return v

        return None
