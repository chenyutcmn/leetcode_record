#不带返回值的算法不适用递归
#思路正确，但是换个角度问题会更明了
#从后向前扫描找到第一个V型结构点


#原始算法从前往后
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #若为空或长度为1，不做处理
        if nums == [] or len(nums) == 1:
            pass
        #若长度为二，两者调转
        elif len(nums) == 2:
            print(3)
            nums[0] , nums[1] = nums[1] , nums[0]
        #长度大于等于3
        else:
            #若存在下一排列
            if self.isHaveNext(nums):
                print(1)
                if self.isHaveNext(nums[1:]):
                    print(2)
                    self.nextPermutation(nums[1:])
                #特殊情况，在nums[0]固定的情况下，nums[1:]已不存在下一排列
                #将nums[0]插入适当位置，逆转nums[1:]
                else:
                    indx = self.findIndx(nums)
                    nums[0] , nums[indx] = nums[indx] , nums[0]
                    nums[1:].reverse()
            #不存在下一排列
            else:
                nums.reverse()
                
    def isHaveNext(self , nums):
        i = 0
        while i < len(nums) - 1 and nums[i] >= nums[i + 1]:
            i += 1
        if i == len(nums) - 1:
            return False
        else:
            return True
    def findIndx(self , nums):
        temp = nums[0]
        for i in range(1 , len(nums) - 1):
            if nums[i] > temp and temp > nums[i + 1]:
                return i
        return len(nums) - 1

#改进型，从后往前扫描，需要考虑的分支只有一条
#JAVA描述
public class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}