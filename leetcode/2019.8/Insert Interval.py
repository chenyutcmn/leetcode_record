## 方案一
class Solution:
    def insert(self, intervals , newInterval):
        if intervals == []:
            return [newInterval]
        n = self.findIndx(intervals , newInterval)
        if n == -1:
            intervals.append(newInterval)
            return intervals
        temp = [newInterval , intervals[n]]
        del intervals[n]
        temp = self.merge(temp)
        if len(temp) == 2:
            intervals.insert(n , temp[0])
            intervals.insert(n+1 , temp[1])
            return intervals
        else:
            return self.insert(intervals , temp[0])

    def findIndx(self , intervals , newInterval):
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1]:
                return i
        return -1
            

    def merge(self , temp):
        if temp[0][1] < temp[1][0]:
            return temp
        else:
            return [[min(temp[0][0] , temp[1][0]) , max(temp[0][1] , temp[1][1])]]

##方案二 思路与方案一相同，但使用栈操作后，时间复杂度将为O(n1)
##自身思路的盲点在于一趟扫描后其实就能了解哪些位置是绝对不可能合并的，这时整个列表其实已经可以部分排序了
def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        stack = []
        for i in range(len(intervals) - 1, -1, -1):
            stack.append(intervals[i])
            
        res = []
        while stack:
            cur_interval = stack.pop()
            # Left ouf of bounds
            if cur_interval[0] > newInterval[1]:
                res.append(newInterval)
                # Update newInterval to be cur_interval to ensure we always come into this condition because there is no more merging that will happen after newInterval has been appended so we keep appending the previous interval
                newInterval = cur_interval
            # Right out of bounds
            elif cur_interval[1] < newInterval[0]:
                res.append(cur_interval)
            else:
                newInterval = [min(cur_interval[0], newInterval[0]), max(cur_interval[1], newInterval[1])]
        # Append the last interval which will be the fully merged newInterval or the last cur_interval from the last iteration
        res.append(newInterval)
        return res


if __name__ == "__main__":
    var = Solution()
    print(var.insert([[1,2],[3,5],[6,7],[8,10],[12,16]] ,  [4,8]))

