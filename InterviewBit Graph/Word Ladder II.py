from collections import deque

class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        if start == end:
            return [[start]]
        st = set(dictV)
        res = []
        qu = deque([(start,)])
        while qu:
            e = qu.popleft()
            for i in range(len(e[-1])):
                if e[-1][i] != end[i]:
                    s = e[-1][:i] + end[i] + e[-1][i+1:]
                    if s not in st:
                        continue
                    if s == end:
                        res.append(list(e + (s,)))
                    else:
                        qu.append(e + (s,))
        return res

