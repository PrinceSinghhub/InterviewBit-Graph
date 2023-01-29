from queue import Queue


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        bucket_hash = {}
        for [a, b] in B:
            if a not in bucket_hash:
                bucket_hash[a] = []
            if b not in bucket_hash:
                bucket_hash[b] = []
            bucket_hash[a].append(b)
            bucket_hash[b].append(a)

        visited = [0] * (A + 1)
        queue = []
        for node in bucket_hash:

            if visited[node] != 0:
                continue

            visited[node] = 1
            queue.append((node, visited[node]))
            while queue:

                (cur_node, color) = queue.pop()

                for neighbour in bucket_hash[cur_node]:

                    if visited[neighbour] == 0:
                        visited[neighbour] = -color
                        queue.append((neighbour, -color))
                    elif visited[neighbour] == color:
                        return 0

        return 1
