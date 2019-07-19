class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        ans = [intervals[0]]
        for i in range(1 , len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][0] = min(ans[-1][0] , intervals[i][0])
                ans[-1][1] = max(ans[-1][1] , intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans

if __name__ == "__main__":
    var = Solution()
    print(var.merge([[1,4],[0,4]]))