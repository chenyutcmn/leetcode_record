class Solution:
    def subsets(self, nums):
        res = []
        for i in range(1, len(nums)+1):
            res += self.help(nums, i)
        return res

    def help(self, n, k):
        if k == 0:
            return [[]]
        if len(n) == k:
            return [n]
        if len(n) < k:
            return []
        if k == 1:
            return [[x] for x in n]
        ret = []
        for i, x in enumerate(n):
            temp = n[i+1:]
            res = self.help(temp, k-1)
            ans = [[x] for i in range(len(res))]
            print(ans)
            ans = [ans[i]+res[i] for i in range(len(ans))]
            ret += ans
        return ret
        
if __name__ == "__main__":
    var = Solution()
    print(var.subsets([1,2,3]))