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



