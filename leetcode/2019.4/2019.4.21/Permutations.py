#了解到了itertools这一模块
class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        ans = []
        for indx , ch in enumerate(nums):
            print(nums[:indx] + nums[indx+1:])
            res = self.permute(nums[:indx] + nums[indx+1:])
            for item in res:
                item.append(ch)
                ans.append(item)
        return ans

if __name__ == "__main__":
    var = Solution()
    print(var.permute([]))