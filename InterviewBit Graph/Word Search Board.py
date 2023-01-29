class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        m, n = len(A), len(A[0])
        def rec(r,c,i):
            if i==len(B)-1 and A[r][c]==B[i]:
                return True
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and B[i+1]==A[nr][nc]:
                    if rec(nr,nc,i+1):
                        return True
            return False
        for row in range(m):
            for col in range(n):
                if A[row][col]==B[0]:
                    if rec(row,col,0):
                        return 1
        return 0
