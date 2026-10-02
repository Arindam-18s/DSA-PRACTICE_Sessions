def permutations(open, close, n, current_perm, output):
    if len(current_perm) == 2 * n:
        output.append(current_perm)
        return
    if open < n:
        permutations(open + 1, close, n, current_perm + "(", output)
    if close < open:
        permutations(open, close + 1, n, current_perm + ")", output)
    return output


# if __name__ == "__main__":
#     n = 3
#     # Output: ["((()))","(()())","(())()","()(())","()()()"]
#     print(permutations(0, 0, n, "", []))


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
