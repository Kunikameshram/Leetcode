class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # Edge case: grid is entirely empty (contains only 0s)
        if all(grid[r][c] == 0 for r in range(rows) for c in range(cols)):
            return 0
        q = collections.deque()
        visited = set()
        minute = -1
        def rotten(r,c):
            if(r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 0):
                return
            grid[r][c] = 2
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append([r,c])
                    visited.add((r,c))
        
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rotten(r+1, c)
                rotten(r-1, c)
                rotten(r, c+1)
                rotten(r, c-1)
            minute +=1    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                
        return minute 