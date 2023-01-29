class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c = 0
        x = [0] * len(A)
        for i in range(len(A) - 1, 0, -1):
            c = max(c, x[A[i]] + x[i] + 1)
            x[A[i]] = max(x[A[i]], x[i] + 1)

        return c
