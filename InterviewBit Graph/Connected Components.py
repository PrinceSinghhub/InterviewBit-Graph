class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        cc = [-1] * A
        E = [[] for _ in range(A)]
        for e in B:
            a, b = e[0] - 1, e[1] - 1
            E[a].append(b)
            E[b].append(a)

        def dfs(x, id):
            st = [x]
            while st:
                cur = st.pop()
                cc[cur] = id
                for nxt in E[cur]:
                    if cc[nxt] == -1:
                        st.append(nxt)

        cnt = 0
        for i in range(A):
            if cc[i] == -1:
                cnt += 1
                dfs(i, cnt)
        return cnt

