#思路一：堆排序输出，超时
#思路二：向大佬学习，orz

class Solution:
    def firstMissingPositive(self, nums) -> int:
        print(nums)
        minpos = 1
        length = len(nums)
        self.sort(nums)
        print(nums)
        while nums[0] <= minpos and length > 0:
            if nums[0] < minpos:
                nums[0] , nums[length - 1] = nums[length - 1] , nums[0]
                print(nums)
                length -= 1
                self.adjust(nums , 0 , length)
            elif nums[0] == minpos:
                nums[0] , nums[length - 1] = nums[length - 1] , nums[0]
                print(nums)
                length -= 1
                self.adjust(nums , 0 , length)
                minpos += 1
        return minpos
                
                        
    def sort(self , nums):
        length = len(nums)
        for i in range(length//2 , -1 , -1):
            self.adjust(nums , i , length)
    def adjust(self , nums , indx , length):

        temp = nums[indx]
        if indx*2 < length and temp > nums[indx*2]:
            temp = nums[indx*2]
        elif indx*2+1 < length and temp > nums[indx*2+1]:
            temp = nums[indx*2+1]
        if temp != nums[indx]:
            if indx*2 < length and temp == nums[indx*2]:
                nums[indx] , nums[indx*2] = nums[indx*2] , nums[indx]
                self.adjust(nums , indx*2 , length)
            else:
                nums[indx] , nums[indx*2+1] = nums[indx*2+1] , nums[indx]
                self.adjust(nums , indx*2+1 , length)


 def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
                
if __name__ == "__main__":
    var = Solution()
    print(var.firstMissingPositive([9,7, 6, 8,11,12]))