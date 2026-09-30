from collections import deque


def detect_cycle_BFS(current_node, adj_list, visited):
    visited[current_node] = True
    Q = deque()
    Q.append([current_node, False])     # [Current_node, Parent_node]
    while Q:
        current_node = Q.popleft()
        current_child_node = current_node[0]
        current_parent_node = current_node[1]

        for neighbour in adj_list[current_child_node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                Q.append([neighbour, current_child_node])
            elif current_parent_node != neighbour:
                print("This Lad is the Cyclist node : ", neighbour)
                return True
    return False


if __name__ == "__main__":
    n = 9
    adj_list = [[], [2, 3], [1, 4], [1], [2], [6], [5], [8, 9], [7, 9], [7, 8]]
    visited = [False] * (n + 1)  # 1-based Indexing

    has_cycle = False
    for i in range(1, n + 1):  # 1-based Indexing
        if not visited[i]:
            if detect_cycle_BFS(i, adj_list, visited):
                has_cycle = True
                break
    # print("There is a Cycle Lads" if has_cycle else "No Cyclists Are there it seems")

# --------------------------------------------------------------------------------------


def detect_cycle_DFS(current_node, parent, adj_list, visited):
    visited[current_node] = True

    for neighbour in adj_list[current_node]:
        if not visited[neighbour]:
            if detect_cycle_DFS(neighbour, current_node, adj_list, visited):
                return True  # Supplying the News of detecting a Cycle To the Root DFS Call
        elif neighbour != parent:
            print("This Lad is the Cyclist node : ", neighbour)
            return True  # Actually Finds the cycle Here
    return False


if __name__ == "__main__":
    n = 9
    adj_list = [[], [2, 3], [1, 4], [1], [2], [6], [5], [8, 9], [7, 9], [7, 8]]
    visited = [False] * (n + 1)
    current_node = 1  # Starting Node

    has_cycle = False
    for i in range(1, n + 1):
        if not visited[i]:
            if detect_cycle_DFS(i, False, adj_list, visited):
                has_cycle = True
                break

    if has_cycle:
        print("Lads Found a Cycle Even With .DFS, AhaHaahaahhahha")
    else:
        print("Lads Couldn't Find a Cycle Even With .DFS, Uhunnhunhnnnnnn")

# --------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
