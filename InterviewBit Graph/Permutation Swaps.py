class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of list of integers
    # @return an integer
      def solve(self, A, B, C):
        def get_root(num):
            while parent[num]!=-1:
                num=parent[num]
            return num
        n=len(A)
        if n!=len(B):
            return 0
        parent=[-1 for i in range(0,n+1)]
        for x,y in C:
            x=A[x-1]
            y=A[y-1]
            while parent[x]!=-1:
                x=parent[x]
            while parent[y]!=-1:
                y=parent[y]
            if x>y:
                parent[y]=x
            if x<y:
                parent[x]=y
        for a,b in zip(A,B):
            if get_root(a)!=get_root(b):
                return 0
        return 1
