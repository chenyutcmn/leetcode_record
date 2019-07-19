import itertools
class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 1:
            return [nums]
        ans = []
        for indx , ch in enumerate(nums):
            print(nums[:indx] + nums[indx+1:])
            res = self.permuteUnique(nums[:indx] + nums[indx+1:])
            for item in res:
                item.append(ch)
                if item not in ans:
                    ans.append(item)
        return ans


if __name__ == "__main__":
    var = Solution()
    print(var.permuteUnique([1,1,2]))