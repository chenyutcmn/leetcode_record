#xrange()返回一个生成器，在list较大时性能较range()更优
#更正，在python3中xrange()与range()合并为range()

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        pre_sum = None
        for i in range(len(nums) - 2):
            head, tail = i+1, len(nums)-1
            while head < tail:
                sum = nums[i] + nums[head] + nums[tail]
                if pre_sum == None:
                    pre_sum = sum
                if abs(sum - target) < abs(pre_sum - target):
                    pre_sum = sum

                if sum < target:
                    head += 1
                elif sum > target:
                    tail -= 1
                else:
                    return target
        return pre_sum