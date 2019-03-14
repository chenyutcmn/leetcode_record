class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"}
        res = []
        for ch in dic[digits[0]]:
            res.append(ch)
        for i in range(1 , len(digits)):
            res = self.getres(res , dic[digits[i]])
        return res
    def getres(self , liststr , string):
        res = []
        for eachstr in liststr:
            for i in range(len(string)):
                res.append(eachstr + string[i])
        return res