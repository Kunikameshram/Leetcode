class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        maxArea = 0

        rows, cols, = len(grid), len(grid[0])

        def bfs(r, c, maxArea):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            maxArea = 1
            

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r, new_c = row+dr, col+dc
                    if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited):
                        maxArea+=1
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            return maxArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r, c, maxArea))
        return maxArea


