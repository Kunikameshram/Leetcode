class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n = cols, m = rows
        row = [1] * n #initialize the last row with 1 

        for i in range(m-1): #this loop will run for all the rows
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]

        # another sol
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.initialize_grid(m, n)
        for row in range(1, m):
            for col in range(1, n):
                self.grid[row][col] = self.grid[row-1][col] + self.grid[row][col-1]
        print(self.grid)
        return self.grid[-1][-1]


    def initialize_grid(self, m, n):
        self.grid = []
        for row in range(m):
            self.grid.append([0 for _ in range(n)])
        for col in range(n):
            self.grid[0][col] = 1
        for row in range(m):
            self.grid[row][0] = 1