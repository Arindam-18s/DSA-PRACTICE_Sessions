# -- Storing Directed and Undirected Graphs --
#-------------------------------------------------------
# **  MATRIX WAY  ** - Space - O(V²) -> Where V = no. of Vertices(NODES) - Very Costly Opr.

def graph_matrix_way_insertion():
    n, m = 5, 6   # n = no. of Nodes | m = no. of Edges
    adj = [[0 for _ in range(n)] for _ in range(n)] # Create a 5x5 grid filled with 0s

    for i in range(m):
        u = int(input('hey give the first node : '))
        v = int(input('hey give the second node : '))
        
        adj[u - 1][v - 1] = 1       # Mark the intersection as 1 (connected)
        adj[v - 1][u - 1] = 1

    print("\nAdjacency Matrix:")
    for row in adj:
        print(row)

# ------------------------------------------------------
# **  LIST WAY  ** - Space - O(V + E) -> Where V = no. of Vertices(NODES), E = no. of Edges - We will use this, Much efficient Spacewise.

def graph_list_way_insertion():
    n, m = 5, 6   # n = no. of Nodes | m = no. of Edges
    adj_list = [[] for _ in range(n + 1)]     # Create an empty list for each of the 5 nodes

    for i in range(1, m + 1):
        u = int(input('hey give the first node : '))
        v = int(input('hey give the second node : '))
        
        # For 1-based indexing, subtract 1 to fit 0-indexed Python lists
        # Store the neighbor directly in the list
        adj_list[u].append(v)
        adj_list[v].append(u)  # Remove this line if the graph is DIRECTED
    print(adj_list)

    print("\nAdjacency List:")
    for node, neighbors in enumerate(adj_list):
        print(f"Node {node} is connected to: {neighbors}")

# ---------------------------------------------------------------------------------------------------
# Breadth Firat Search(BFS) - Level Order Traversal - O(N x E) N = np. of nodes, E = no. of edgess

from collections import deque
def BFS(n, adj_list):
    Q = deque()
    visited = [False] * n
    Q.append(1)                                     # Starting node is visited first
    visited[1] = True                               # Appending the starting node
    bfs_result = []

    while Q:
        current_node = Q.popleft()                  # Head Of the Q
        bfs_result.append(current_node)

        for neighbour in adj_list[current_node]:    # Finds the neightbours of the current node by fetching elements 
            if not visited[neighbour]:              # from the adj_list, where current node is the index of the adj_list 
                Q.append(neighbour)                 # and its neightbours are the stored elements at that index
                visited[neighbour] = True
    return bfs_result

if __name__ == "__main__":
    n = 8
    adj_list = [[], [2, 6], [1, 3, 4], [2], [2],[7], [1, 7, 8], [5, 6], [6]]
    # print(BFS(n + 1, adj_list))

# ---------------------------------------------------------------------------------------------------
# Depth Firat Search(DFS) - Depth Order Traversal - O(N) + O(2 x E) N = no. of nodes, E = no. of edgess

def DFS(current_node, visited, adj_list, dfs_result):       # RECURSIVE Soln.
    visited[current_node] = True                            # Visit the current Node
    dfs_result.append(current_node)                         # Add the Current Node to the DFS Traversal result

    for neighbour in adj_list[current_node]:                # Finds the neightbours of the current node by fetching elements 
        if not visited[neighbour]:                          # from the adj_list, where current node is the index of the adj_list 
            DFS(neighbour, visited, adj_list, dfs_result)   # and its neightbours are the stored elements at that index
            visited[neighbour] = True

if __name__ == "__main__":
    n = 8
    adj_list = [[], [2, 3], [1, 5, 6], [1, 4, 7], [3, 8], [2], [2], [3, 8], [4, 7]]
    visited = [False] * (n + 1)     # For 1 Based Indexing
    current_node = 1                # Starting Node
    dfs_result = []
    # DFS(current_node, visited, adj_list, dfs_result)
    # print(dfs_result)

# ---------------------------------------------------------------------------------------------------
# Detect a Cycle in Any Kind of Undirected Graph - Time -> O(N + 2E) Space-> O(N) N = no. of nodes, E = no. of edgess
# BFS Implementation
from collections import deque
def detect_cycle_BFS(source_node, adj_list, visited):
    visited[source_node] = True
    Q = deque()                         # BFS Implementation 
    Q.append([source_node, -1])
    while Q:
        current_node = Q.popleft()
        current_child_node = current_node[0]
        current_parent_node = current_node[1]

        for neighbour in adj_list[current_child_node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                Q.append([neighbour, current_child_node])
            elif(current_parent_node != neighbour):
                return True
    return False

if __name__ == "__main__":
    n = 9
    adj_list = [[], [2, 3], [1, 4], [1], [2], [6], [5], [8, 9], [7, 9], [7, 8]]
    visited = [False] * (n + 1)         # 1-based Indexing
    has_cycle = False
    for i in range(1, n + 1):           # 1-based Indexing
        if not visited[i]:
            if detect_cycle_BFS(i, adj_list, visited):
                has_cycle = True
                break
    print("There is a Cycle Lads" if has_cycle else "No Cyclists Are there it seems")

# ---------------------------------------------------------------------------------------------------
# Detect a Cycle in Any Kind of Undirected Graph - Time -> O(N + 2E) Space-> O(N) N = no. of nodes, E = no. of edgess
# DFS Implementation

def detect_cycle_DFS(current_node, parent, adj_list, visited):      # DFS Implementation
    visited[current_node] = True

    for neighbour in adj_list[current_node]:
        if not visited[neighbour]:
            if detect_cycle_DFS(neighbour, current_node, adj_list, visited):
                return True     # Supplying the News of detecting a Cycle To the Root DFS Call
        elif (neighbour != parent):
            print("This Lad is the Cyclist node : ", neighbour)
            return True         # Actually Finds the cycle Here
    return False

if __name__ == "__main__":      # DFS Implementation
    n = 9
    adj_list = [[], [2, 3], [1, 4], [1], [2], [6], [5], [8, 9], [7, 9], [7, 8]]
    visited = [False] * (n + 1)
    current_node = 1        # Starting Node

    has_cycle= False
    for i in range(1, n + 1):
        if not visited[i]:
            if (detect_cycle_DFS(i, -1, adj_list, visited)):
                has_cycle = True
                break
                
    if has_cycle:
        print("Lads Found a Cycle Even With .DFS, AhaHaahaahhahha")
    else:
        print("Lads Couldn't Find a Cycle Even With .DFS, Uhunnhunhnnnnnn")

# ---------------------------------------------------------------------------------------------------
# LeetCode - 2608. Shortest Cycle in a Graph - Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]] | Output: 3
# Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 | Time: O(V · (V + E)) , Space: O(V + E) 
                                                                         # N = no. of nodes, E = no. of edgess
from collections import deque
def detect_cycle_BFS(source_node, adj_list, n):
    dist = [-1] * (n)
    Q = deque()
    Q.append([source_node, -1])     # [Current_node, Parent_node]
    dist[source_node] = 0
    current_cycle_length = float("inf")

    while Q:
        current_node = Q.popleft()
        current_child_node, current_parent_node = current_node[0], current_node[1]

        for neighbour in adj_list[current_child_node]:
            if dist[neighbour] == -1:
                dist[neighbour] = dist[current_child_node] + 1
                Q.append([neighbour, current_child_node])
            elif current_parent_node != neighbour:
                # closed a cycle: path to child + path to neighbour + this edge
                local_cycle_length = dist[neighbour] + dist[current_child_node] + 1
                current_cycle_length = min(current_cycle_length, local_cycle_length)
    return current_cycle_length

if __name__ == "__main__":
    n = 9
    adj_list = [[], [2, 3], [1, 4], [1], [2], [6], [5], [8, 9], [7, 9], [7, 8]]

    min_shortest_path = float("inf")
    for i in range(n + 1):      # BFS from EVERY node, fresh dist each time
        shortest_path = detect_cycle_BFS(i, adj_list, n + 1)
        min_shortest_path = min(shortest_path, min_shortest_path)
    print(-1 if min_shortest_path == float("inf") else "Shortest Cycles Length is  : ", min_shortest_path)

# ---------------------------------------------------------------------------------------------------
# 200. Number of Islands - DFS Appr. Time - O(N x M); Space - O(N x M)
#                  ->  Testcase - [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
                     # O/p - 1      ''''''''''''''         '''''      '''       '''''''
def DFS(grid, i, j):
    if ( i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" ):  # 0 - Means Water Body
        return  # Base Case
    grid[i][j] = "0"  # Marking the cell as Visited By Making it a water Body
    DFS(grid, i + 1, j)
    DFS(grid, i - 1, j)
    DFS(grid, i, j + 1)
    DFS(grid, i, j - 1)

if __name__ == "__main__":  # Number of Islands
    grid = [                            #     grid = [
        ["1", "1", "0", "0", "0"],      #               ["| Visited", "Visited |",     "~"     ,     "~"     ,     "~"     ],  
        ["1", "1", "0", "0", "0"],      #               ["| Visited", "Visited |",     "~"     ,     "~"     ,     "~"     ],
        ["0", "0", "1", "0", "0"],      #               [     "~"   ,     "~"    ,"| Visited |",     "~"     ,     "~"     ],
        ["0", "0", "0", "1", "1"],      #               [     "~"   ,     "~"    ,     "~"     , "| Visited" , "Visited |" ],
    ]
    count = 0  # Tracks the no. of islands
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                DFS(grid, i, j)
                count += 1
    print(count)

# ---------------------------------------------------------------------------------------------------










# ---------------------------------------------------------------------------------------------------










# ---------------------------------------------------------------------------------------------------









# ---------------------------------------------------------------------------------------------------


