class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        temp = 0
        i = 0
        left = 0
        right = 0
        while i < len(S):
            if S[i] == '(':
                left += 1
            if S[i] == ')':
                right += 1
            print(left , right)
            if left == right: 
                res += S[temp + 1 : i]
                print(res)
                temp = i + 1
            i += 1
        return res

var = Solution()
print(var.removeOuterParentheses("(()())(())"))