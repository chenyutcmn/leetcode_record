#一遍过 开心


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        for indx , ch in enumerate(strs[0]):
            for i in range(1 , len(strs)):
                if indx >= len(strs[i]) or ch != strs[i][indx]:
                    return res
            res += ch
        return res
        