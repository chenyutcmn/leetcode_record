# 方法一 垃圾
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m
        if m == n:
            return self.uniquePaths(m - 1 , n) * 2
        return self.uniquePaths(m - 1 , n) + self.uniquePaths(m , n - 1)
    
#方法二 dp
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(m)] for _ in range(n)]
        print(dp)
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

#方法三 看不懂 orz
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fm=math.factorial(m-1)
        fn=math.factorial(n-1)
        fmn=math.factorial(m+n-2)
        return int(fmn/(fn*fm))
if __name__ == "__main__":
    var = Solution()
    print(var.uniquePaths(23 , 12))