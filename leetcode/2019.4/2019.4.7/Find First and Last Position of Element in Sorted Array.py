class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1 , -1]
        if nums[0] > target or nums[-1] < target:
            return [-1 , -1]
        mid = len(nums) // 2
        if nums[mid] == target:
            i = j = mid
            while i >= 0 and nums[i] == target:
                i -= 1
            while j < len(nums) and nums[j] == target:
                j += 1
            return [i + 1 , j - 1]
        elif nums[mid] < target:
            res = self.searchRange(nums[mid + 1:] , target)
            for i in range(len(res)):
                if res[i] == -1:
                    break
                res[i] += (mid + 1)
            return res
        elif nums[mid] > target:
            return self.searchRange(nums[:mid] , target)
        
