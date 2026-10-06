# # Topological Sort - A topological ordering is a linear ordering of the vertices
# # such that for every directed edge u -> v, vertex u appears before vertex v in the ordering.

# from collections import deque
# class Solution:
#     def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
#         # Code here
#         inDegree = [0] * V
#         adj_list = [[] for _ in range(V)]
#         for u, v in edges:
#             adj_list[u].append(v)

#         for i in range(V):
#             for neighbour in adj_list[i]:
#                 inDegree[neighbour] += 1

#         Q = deque()
#         for j in range(V):
#             if inDegree[j] == 0:
#                 Q.append(j)

#         TopoSort = []
#         while Q:
#             current_node = Q.popleft()
#             TopoSort.append(current_node)

#             for neighbour in adj_list[current_node]:
#                 inDegree[neighbour] -= 1
#                 if inDegree[neighbour] == 0:
#                     Q.append(neighbour)

#         return TopoSort

s = "()))(("

stack = [0]
count = 0
for i  in range(len(s)):
    if s[i] == "(":
        stack[0] += 1
    else:
        if stack[0] > 0:
            stack[0] -= 1
        else:
            count += 1

if stack:
    count += stack[0]

print(count)