class Solution:

    def _dfs(self, curr, graph, good_nodes, visited, moves):
        if curr in good_nodes:
            return

        visited[curr] = True
        next_node = graph[curr - 1]

        if next_node in good_nodes:
            good_nodes[curr] = 1
            return

        if not visited[next_node]:
            self._dfs(next_node, graph, good_nodes, visited, moves)
        else:
            good_nodes[next_node] = 1
            moves[0] += 1

        good_nodes[curr] = 1
        return

        # @param A : list of integers

    # @return an integer
    def solve(self, graph):
        good_nodes = {}
        good_nodes[1] = 1
        num = len(graph)
        visited = [False] * (num + 1)
        moves = [0]

        for i in range(1, num + 1):
            self._dfs(i, graph, good_nodes, visited, moves)

        return moves[0]

