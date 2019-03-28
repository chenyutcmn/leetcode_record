#若思路过于复杂，重新想！！！！！
#原思路，找出s中每一个合法子序列，比较他们的长度
#暴力求解思路，以2,3,4,...,n长度为模板去套s，找到最长子序列
#dp思路，一趟扫描，跟新当前指针长度下最长子序列长度
#trick，两趟扫描，从左到右和从右到左，具体见以下代码

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,0
        max_ = 0
        for i in range(len(s)):
            if s[i] == '(':
                l +=1
            else:
                r +=1
            if l == r:
                max_ = max(max_, 2 * r)
            else:
                if r >= l:
                    l = r = 0
        l,r = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, 2 * l)
            else:
                if l >= r:
                    l = r = 0
        return max_