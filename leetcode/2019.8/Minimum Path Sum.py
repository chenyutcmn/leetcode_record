class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        temp = [[0 for _ in range(n)] for _ in range(m)]
        temp[0][0] = grid[0][0]
        for i in range(1 , n):
            temp[0][i] = temp[0][i - 1] + grid[0][i]
        for i in range(1 , m):
            temp[i][0] = temp[i - 1][0] + grid[i][0]
        for i in range(1 , m):
            for j in range(1 , n):
                temp[i][j] = min(temp[i - 1][j] , temp[i][j - 1]) + grid[i][j]
        
        return temp[-1][-1]