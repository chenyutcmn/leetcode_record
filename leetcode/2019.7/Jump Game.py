class Solution:
    def canJump(self, nums) -> bool:
        return self.help(nums , len(nums) - 1)
    def help(self , nums , indx):
        print(indx)
        if indx == 0:
            return True
        if nums[indx - 1] > 0:
            return self.help(nums , indx - 1)
        else:
            print("this is temp")
            temp = indx - 2
            print(temp)
            while temp >= 0:
                if nums[temp] + temp >= indx:
                    return self.help(nums , temp)
                else:
                    temp -= 1
            return False

if __name__ == "__main__":
    var = Solution()
    print(var.canJump([6,0 , 0,0,0,0,0,4]))