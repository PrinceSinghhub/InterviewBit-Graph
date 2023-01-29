class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        for i in range(len(B)):
            if B[i][1] == A:
                return 1;

        return 0
