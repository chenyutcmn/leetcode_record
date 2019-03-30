#七次过，好气哦

class Solution:
    def search(self, nums , target: int) -> int:
        if nums[0] <= nums[-1]:
            indx = 0
        else:
            indx = self.findindx(nums , -1 , len(nums) - 1)
        print(indx)
        return self.getres(nums , indx , indx + len(nums) , target)
        
    def findindx(self , nums , begin , end):
        if begin == end:
            return begin
        mid = (begin + end) // 2
        if nums[mid] > nums[mid + 1]:
            return mid
        elif nums[begin] > nums[mid]:
            return self.findindx(nums , begin , mid)
        else:
            return self.findindx(nums , mid + 1 , end)
    
    def getres(self , nums ,  begin , end , target):
        temp = 0
        if begin == end:
            if begin >= len(nums):
                temp = begin - len(nums)
            else:
                temp = begin
            if nums[temp] == target:
                return temp
            else:
                return -1
        mid = (begin + end) // 2
        if mid >= len(nums):
            temp = mid - len(nums)
        else:
            temp = mid
        if nums[temp] == target:
            return temp
        else:
            if nums[temp] < target:
                return self.getres(nums , mid + 1 , end , target)
            else:
                return self.getres(nums , begin , mid , target)

if __name__ == "__main__":
    var = Solution()
    print(var.search([2,3,4,5,1] , 3))