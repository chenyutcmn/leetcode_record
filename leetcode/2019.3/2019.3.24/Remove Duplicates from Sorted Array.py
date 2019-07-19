class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = nums[0]
        for num in nums[1:]:
            if num == temp:
                nums.remove(num)
            else:
                temp = num
        return len(nums)