#代码不够简洁，多分枝情况下如何统一分支简化代码是一个问题
#Simple is better than complex.
#Complex is better than complicated.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while (i < len(s)) and s[i] == "M":
            res += 1000
            i += 1
        if (i < (len(s) - 1)) and (s[i] == "C") and (s[i + 1] == "M"):
            res += 900
            i += 2
        if (i < (len(s) - 1)) and (s[i] == "C") and (s[i + 1] == "D"):
            res += 400
            i += 2
        if (i < len(s)) and s[i] == "D":
            res += 500
            i += 1
        while (i < len(s)) and s[i] == "C":
            res += 100
            i += 1
        if (i < (len(s) - 1)) and (s[i] == "X") and (s[i + 1] == "C"):
            res += 90
            i += 2
        if (i < (len(s) - 1)) and (s[i] == "X") and (s[i + 1] == "L"):
            res += 40
            i += 2 
        if (i < len(s)) and s[i] == "L":
            res += 50
            i += 1
        while (i < len(s)) and s[i] == "X":
            res += 10
            i += 1
        if (i < (len(s) - 1)) and (s[i] == "I") and (s[i + 1] == "X"):
            res += 9
            i += 2
        if (i < (len(s) - 1)) and (s[i] == "I") and (s[i + 1] == "V"):
            res += 4
            i += 2
        if (i < len(s)) and s[i] == "V":
            res += 5
            i += 1
        while (i < len(s)) and s[i] == "I":
            res += 1
            i += 1
        return res
            
            
                
        