class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = -1
            else:
                for j in range(i , m):
                    obstacleGrid[j][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = -1
            else:
                obstacleGrid[0][i:] = [1 for _ in range(n - i)]
        for i in range(1 , m):
            for j in range(1 , n):
                if obstacleGrid[i][j] != 1:
                    if obstacleGrid[i - 1][j] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if obstacleGrid[i][j - 1] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != 1 else 0

if __name__ == "__main__":
    var = Solution()
    print(var.uniquePathsWithObstacles([[1],[0]]))