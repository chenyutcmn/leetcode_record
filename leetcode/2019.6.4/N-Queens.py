#虽然知道解法，但实现起来还是有难度。大佬的写法简洁中透露着美观，朴素中透露着力量，实在是望其项背，自叹弗如

class Solution:
    def solveNQueens(self, n: int):
        self.res = []
        self.n = n
        self.DFS([] , [] , [])
        return ([["." * i + "Q" + "." * (self.n - i - 1) for i in one_res] for one_res in self.res])
    
    def DFS(self , queens , xy_sum , xy_sub):
        if len(queens) == self.n:
            self.res.append(queens)
            return None
        else:
            for i in range(self.n):
                if (i not in queens) and ((len(queens) + i) not in xy_sum) and ((len(queens) - i) not in xy_sub):
                    self.DFS(queens + [i] , xy_sum + [len(queens) + i] , xy_sub + [len(queens) - i])

if __name__ == "__main__":
    var = Solution()
    print(var.solveNQueens(4))