class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        if target < candidates[0] or (len(candidates) == 1 and target not in candidates):
            return []
        temp = []
        for _ , num in enumerate(candidates):
            if num == target:
                temp.append([num])
            else:
                new_target = target - num
                onetemp = self.combinationSum(candidates , new_target)
                if onetemp != []:
                    for item in onetemp:
                        item.append(num)
                    temp += onetemp
        res = []
        for item in temp:
            item.sort()
            if item not in res:
                res.append(item)
        return res
if __name__ == "__main__":
    var = Solution()
    print(var.combinationSum([2,3,6,7] , 7))