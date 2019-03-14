#k_sum问题 本算法为O(n3)时间复杂度，但类比与其他同复杂度实现，我的算法可以说是耗时超级久！
#存在问题：1. 虽然是递归思想，但是并没有写成递归形式 2.每一次的sort操作耗时太久。搜索的实现也不如双指针搜索快
#总而言之，这是一个看上过去平平无奇，但是仔细一看就会感觉异常垃圾的算法 (๑•̀ㅂ•́)و✧
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            sum3 = target - nums[i]
            resfor3 = self.getsum3(nums[i + 1:], sum3)
            if resfor3 != []:
                for each in resfor3:
                    each.append(nums[i])
                    each.sort()
                    if each not in res:
                        res.append(each)
        return res

    def getsum3(self, nums, target):
        res = []
        for i in range(len(nums) - 2):
            sum2 = target - nums[i]
            resfor2 = self.getsum2(nums[i + 1:], sum2)
            if resfor2 != []:
                for each in resfor2:
                    each.append(nums[i])
                    each.sort()
                    if each not in res:
                        res.append(each)
        return res

    def getsum2(self, nums, target):
        resfor2 = []
        for i in range(len(nums) - 1):
            if (target - nums[i]) in nums[i + 1:]:
                res = []
                res.append(nums[i])
                res.append(target - nums[i])
                res.sort()
                if res not in resfor2:
                    resfor2.append(res)
        return resfor2

        
        