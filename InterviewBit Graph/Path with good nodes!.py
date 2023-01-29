# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10**9)
# def dfs(visited,adj,arr,c,count,u,ans):
#     visited[u]=True
#     if arr[u-1]==1:
#         count +=1
#     if len(adj[u])==0:
#         if count<=c:
#             ans +=1
#     for i in adj[u]:
#         if visited[i]==False:
#             dfs(visited,adj,arr,c,ans,i,count)
# class Solution:
#     # @param A : list of integers
#     # @param B : list of list of integers
#     # @param C : integer
#     # @return an integer
#     def solve(self, A, B, C):
#         adj=defaultdict(list)
#         for i in B:
#             adj[i[0]].append(i[1])
#             adj[i[1]].append(i[0])
#         print(adj)
#         count=0
#         visited=[False]*(len(A)+1)
#         dfs(visited,adj,A,C,count,1,0)
#         return count

class Solution:

    def solve(self, A, B, C):
        self.num_paths = 0

        # Build the graph
        graph = {}
        for edge in B:
            source = edge[1]
            target = edge[0]
            if source not in graph:
                graph[source] = []
            graph[source].append(target)

        def traverse_nodes(graph, source, num_good, A, C):
            # Base case
            if not (source in graph):
                if num_good <= C:
                    self.num_paths += 1
                return

            for target in graph[source]:
                traverse_nodes(graph, target, num_good + (A[target-1]), A, C)

        traverse_nodes(graph, 1, A[0], A, C)
        return self.num_paths
