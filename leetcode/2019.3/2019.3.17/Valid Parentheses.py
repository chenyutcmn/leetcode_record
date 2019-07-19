#这句更简洁
#while "()" in s or "{}" in s or '[]' in s:
#    s = s.replace("()", "").replace('{}', "").replace('[]', "")
#str.find()和str.replace()使用不够熟练
#todo:栈方法实现
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True 
        n = len(s)
        brack = ["(" , ")" , "[" , "]" , "{" , "}"]
        for i in range(len(s) - 1):
            j = brack.index(s[i])
            k = brack.index(s[i + 1])
            if k - j == 1:
                s = s[:i] + s[i + 2:]
                break
        if len(s) != n:
            return self.isValid(s)
        else:
            return False
if __name__ == "__main__":
    var = Solution()
    test = "()"
    print(var.isValid(test))

#def stack_solution():