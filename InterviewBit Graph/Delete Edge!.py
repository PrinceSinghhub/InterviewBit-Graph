#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
adj = []
s = 0
maxe = 0
mod = 1000000007


def dfs(u, p, A):
    global adj, s, maxe, mod
    val = A[u - 1]
    for v in adj[u]:
        if v == p:
            continue
        val += dfs(v, u, A)
    res = val  * ((s - val))
    maxe = max(maxe, res)
    return val


class Solution:

    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer

    def deleteEdge(self, A, B):
        global adj, s, maxe, mod
        s = 0
        maxe = 0
        adj = [[] for i in range(100009)]
        for a in A:
            s += a
        for edge in B:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        dfs(1, 0, A)
        return maxe%mod

