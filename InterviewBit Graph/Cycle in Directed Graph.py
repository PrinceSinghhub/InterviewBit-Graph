from collections import defaultdict


class Solution:

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, root, visit):
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            print(node, visit[node - 1])
            if not visit[node - 1]:
                # print("kk")
                visit[node - 1] = True
                for n in self.dic[node]:
                    # print(n)
                    # if not visit[n-1]:
                    stack.append(n)
            else:
                return True
        return False

    def solve(self, A, B):
        visited = set()

        for ind in B:
            if ind[1] in visited:
                return 1

            visited.add(ind[0])
            # visited.add(ind[1])

        return 0


