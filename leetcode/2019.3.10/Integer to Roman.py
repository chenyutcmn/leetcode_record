#代码不够简洁，多分枝情况下如何统一分支简化代码是一个问题


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        numsplit = []
        chs = "MDCLXVI"
        while num:
            numsplit.append(num % 10)
            num = num // 10
        numsplit.reverse()
        n = len(numsplit)
        for i in range(n):
            if (n - i) == 4: 
                base = "M"
            elif (n - i) == 3:
                base = "C"
            elif (n - i) == 2:
                base = "X"
            elif (n - i) == 1:
                base = "I"
            indx = chs.find(base)
            if numsplit[i] == 9:
                res += base
                res += chs[indx - 2]
            elif 5 <= numsplit[i] < 9:
                res += chs[indx - 1]
                for i in range(numsplit[i] - 5):
                    res += base
            elif numsplit[i] == 4:
                res += base
                res += chs[indx - 1]
            elif 0 <= numsplit[i] < 5:
                for i in range(numsplit[i]):
                    res += base
        return res
                
        