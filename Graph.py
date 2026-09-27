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

def BFS(n : int, adj_list):
    element_storage = deque()
    visited = [False] * n
    visited[1] = True           # Starting node is visited first
    element_storage.append(1)   # Appending the starting node
    bfs_result = []

    while(element_storage):
        node = element_storage.popleft()    # Current Top of the Queue
        bfs_result.append(node)

        # Explore neighbors
        for neighbor in adj_list[node]:     # Finds the neightbours of the current node by fetching elements from the adj_list, 
            if not visited[neighbor]:       # where current node is the index of the adj_list and its neightbours 
                element_storage.append(neighbor)                          # are the stored elements at that index
                visited[neighbor] = True
    return bfs_result

# ---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    n = 8
    adj_list = [[], [2, 6], [1, 3, 4], [2], [2],[7], [1, 7, 8], [5, 6], [6]]
    print(BFS(n + 1, adj_list))
