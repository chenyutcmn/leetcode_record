#滑动窗口的变种

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0 
        end = len(height) - 1
        maxV = min(height[start] , height[end]) * (end - start)
        while start < end:
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            thisV = min(height[start] , height[end]) * (end - start)
            maxV = max(maxV , thisV)
        return maxV