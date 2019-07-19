#典型的DP问题，这次我要自己写，看答案的是狗
#V1版本，超时了！，时间复杂度到达了令人发指的On3！ 下午写V2改进版
#V2版本，去掉了最外层循环，因为发现根本不需要！吗的，早上的我有点愚蠢，复杂度On2。
#还是超时了艹
#V3版本，试图进一步优化
#又超时了，草
#V4版本，这次不过我就看答案
#没有V4了 汪汪
#真香
#此答案未精确求解，而是用一片区域覆盖住了解，大大降低了复杂度。 注意若非必要，勿求解更多信息
class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1 or nums == []:
            return 0
        res = [float("inf") for _ in range(len(nums))]
        #第i阶段，代表终点index为i+1的子序列,res[i]表示从i阶段终点的最小步数
        res[-2] = 1
            #i阶段下，点j到终点的最短步数
        for j in range(len(nums) - 3 , -1 , -1):
            if (len(nums) - j) <= nums[j]:
                res[-1] = 1
            else:
                res[-1] = (len(nums) - 1 - j) - nums[j] + 1            
            #j点经由k点到i阶段终点的步数，res[k]代表从k点到终点的最短步数
            for k in range(j + 1 , len(nums) - 1):
                if (k - j) <= nums[j]:
                    res[-1] = min(res[-1] , res[k] + 1)
                else: 
                    res[-1] = min(res[-1] , res[k] + 1 + (k - j - nums[j]))
            #更新从j点到i阶段终点的最短步数
            res[j] = res[-1]
        return res[0]

    def jump3(self, nums) -> int:
        if len(nums) == 1 or nums == []:
            return 0
        res = [float("inf") for _ in range(len(nums))]
        #第i阶段，代表终点index为i+1的子序列,res[i]表示从i阶段终点的最小步数
        res[-1] = 0
            #i阶段下，点j到终点的最短步数
        for j in range(len(nums) - 2 , -1 , -1): 
            if nums[j] == 0:
                continue
            end = j + nums[j] + 1
            if end >= len(nums):
                res[j] = 1
            else:
                print("here")
                res[j] = min(res[j + 1 : end]) + 1
        return res[0]

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

