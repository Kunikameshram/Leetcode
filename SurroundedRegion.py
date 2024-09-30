class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        edge = set()
        q = collections.deque()
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            edge.add((r, 0))
            edge.add((r, cols-1))
        for c in range(cols):
            edge.add((0, c))
            edge.add((rows-1, c))

        def bfs():
            while q:
                r, c = q.popleft()
                direction = [[1,0], [-1, 0], [0, -1], [0, 1]]
                for dr, dc in direction:
                    nr, nc = dr + r, dc + c
                    if (nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r, c in edge:
            if board[r][c] == "O" and (r, c) not in visited:
                visited.add((r, c))
                q.append((r, c))
                bfs()
                
        edge = edge.union(visited)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in edge:
                    board[r][c] = "X"
    