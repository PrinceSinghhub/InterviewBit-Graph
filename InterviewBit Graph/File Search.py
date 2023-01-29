class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def breakRecords(self, A, B):
        rank = [1 for i in range(A + 1)]
        par = [i for i in range(A + 1)]

        def find(n):
            val = n
            while par[val] != val:
                par[val] = par[par[val]]
                val = par[val]
            return val

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] = rank[p2] + 1
            else:
                par[p1] = p2
                rank[p2] = rank[p1] + 1
            return 1

        res = A
        for n1, n2 in B:
            res = res - union(n1, n2)
        return res



