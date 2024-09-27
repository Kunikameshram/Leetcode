#Walls and gates or Treasure and island

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        def expand(r, c):
            if(r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == -1):
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
    
            
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                expand(r+1, c)
                expand(r-1, c)
                expand(r, c+1)
                expand(r, c-1)
            dist += 1



