from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1

        time = 0
        # Directions for BFS: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))

        return time if fresh_count == 0 else -1