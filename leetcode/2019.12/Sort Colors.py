class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = -1
        w = -1
        b = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if w == -1 and b == -1:
                    r = i
                elif w == -1 or b == -1:
                    if w == -1:
                        r += 1
                        b = i
                        nums[r] = 0
                        nums[b] = 2
                    if b == -1:
                        r += 1
                        w = i
                        nums[r] = 0
                        nums[w] = 1
                else:
                    r += 1
                    w += 1
                    b = i
                    nums[r] = 0
                    nums[w] = 1
                    nums[b] = 2
            elif nums[i] == 1:
                if r == -1 and b == -1:
                    w = i 
                elif r == -1 or b == -1:
                    if r == -1:
                        w += 1
                        b = i
                        nums[w] = 1
                        nums[b] = 2
                    if b == -1:
                        w = i
                        nums[w] = 1
                else:
                    if w == -1:
                        w = r + 1
                    else:
                        w += 1
                    b = i
                    nums[w] = 1
                    nums[b] = 2

            elif nums[i] == 2:
                b = i

if __name__ == "__main__":
    var = Solution()
    nums = [2,0,2,1,1,0]
    var.sortColors(nums)
    print(nums)