#即使之前就知道解法，也做了一个小时。fxxk

class Solution:
    def trap(self, height: List[int]) -> int:
        return self.help(height , 0 , len(height) - 1)
            
    def help(self , height , begin , end):
        if (end - begin) < 2:
            return 0
        indx = self.find_indx(height , begin , end)
        if indx == -1:
            ans = 0
            for i in range(begin + 1 , end):
                ans += min(height[begin] , height[end]) - height[i]
            return ans
        else:
            return self.help(height , begin , indx) + self.help(height , indx , end)
        
    def find_indx(self , height , beg , end):
        temp = min(height[beg] , height[end])
        indx = -1
        for i in range(beg + 1 , end):
            if height[i] > temp:
                temp = height[i]
                indx = i
        return indx