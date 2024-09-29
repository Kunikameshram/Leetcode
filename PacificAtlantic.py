class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        q = collections.deque()
        res = []
        
        rows, cols = len(heights), len(heights[0])
            
        for r in range(rows):
            pacific.add((r, 0))
            atlantic.add((r, cols-1))
            
        for c in range(cols):
            atlantic.add((rows-1, c))
            pacific.add((0, c))

        def bfs(current):
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_r, new_c = r+dr , c+dc
                    if new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in current and heights[new_r][new_c] >= heights[r][c]:
                        q.append((new_r, new_c))
                        current.add((new_r, new_c))

        for r, c in pacific:
            q.append((r,c))
        bfs(pacific)
            
        for r, c in atlantic:
            q.append((r,c))
        bfs(atlantic)

        for pair in atlantic:
            if pair in pacific:
                res.append(list(pair))
        return res