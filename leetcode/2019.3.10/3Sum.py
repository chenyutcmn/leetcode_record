import collections

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = collections.defaultdict(lambda: 0)
        pos, neg, ret = [], [], []
        
        for num in nums:
            count[num] += 1
            if count[num] == 1:
                pos.append(num) if num >= 0 else neg.append(num)
                
        if count[0] >= 3: ret.append([0, 0, 0])
        
        pos.sort(), neg.sort()
        
        for idx1 in neg:
            for idx2 in pos:
                idx3 = -idx1 - idx2
                if idx3 in (idx1, idx2) and count[idx3] >= 2:
                    ret.append([idx1, idx2, idx3])
                if idx3 in count and (idx3 > idx2 or idx1 < idx3 < 0):
                    ret.append([idx1, idx2, idx3])
        return ret