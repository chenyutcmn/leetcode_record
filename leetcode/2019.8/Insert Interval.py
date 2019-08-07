class Solution:
    def insert(self, intervals , newInterval):
        if intervals == []:
            return [newInterval]
        n = self.findIndx(intervals , newInterval)
        temp = [newInterval , intervals[n+1]]
        del intervals[n]
        temp = self.merge(temp)
        if len(temp) == 2:
            intervals.insert()
            intervals.insert()
            return intervals
        else:
            self.insert(intervals , temp)

    def findIndx(self , intervals , newInterval):
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][1]:
                return i
        return len(intervals) - 1
            

    def merge(self , temp):
        if temp[0][1] > temp[1][0]:
            return [[temp[0][0] , temp[1][1]]]
        else:
            return temp

