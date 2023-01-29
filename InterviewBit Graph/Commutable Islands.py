from operator import itemgetter


class Solution:

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, edges):
        sets = [i for i in range(0, A + 1)]
        cost = 0
        edges.sort(key=itemgetter(2))
        # print(edges)
        for a, b, dist in edges:
            # print(sets)
            a_set = self.find(sets, a)
            b_set = self.find(sets, b)
            if a_set == b_set:
                continue
            cost += dist
            self.union(sets, a, b, a_set, b_set)
        return cost

    def find(self, sets, a):
        if sets[a] == a:
            return a
        return self.find(sets, sets[a])

    def union(self, sets, a, b, a_set, b_set):
        if a_set < b_set:
            sets[b_set] = a_set
        else:
            sets[a_set] = b_set

