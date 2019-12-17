class Solution:
    def combine(self, n: int, k: int):
        n = [i+1 for i in range(n)]
        return self.help(n, k)

    def help(self, n, k):
        if k == 0:
            return []
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
            ans = [ans[i]+res[i] for i in range(len(ans))]
            ret += ans
        return ret

if __name__ == "__main__":
    var = Solution()
    print(var.combine(4,2))