class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def find_parent(self, parent, i):
        index = i
        while (parent[index] != -1):
            index = parent[index]

        return index

    def merge(self, x, y, parent):
        parent[x] = y

    def solve(self, A, B):
        parent = [-1 for i in range(A)]

        for i in range(len(B)):
            x = B[i][0] - 1
            y = B[i][1] - 1
            setx = self.find_parent(parent, x)
            sety = self.find_parent(parent, y)
            if setx == sety:
                return 1
            else:
                self.merge(setx, sety, parent)

        return 0


