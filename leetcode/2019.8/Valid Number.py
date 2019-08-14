class Solution:
    def isNumber(self, s: str) -> bool:
        num = "0123456789"
        sign = ["+" , "-"]
        num_sta = []
        point_sta = []
        while s != '' and s[0] == ' ':
            s = s[1:]
        while s != '' and s[-1] == ' ':
            s = s[:-1]
        if s == '':
            return False
        for i in range(len(s)):
            if (s[i] not in num) and (s[i] not in sign) and (s[i] != '.' and s[i] != 'e'):
                return False
            if s[i] in sign and i != 0:
                return False
            if s[i] in num:
                num_sta.append(s[i])
            if s[i] == ".":
                num_sta.append(s[i])
                point_sta.append(s[i])
            if s[i] == "e":
                if i == len(s) - 1 or i == 0:
                    return False
                if len(point_sta) > 1 or s[0] == '.' or s[-1] == '.':
                    return False
                s = s[i+1:]
                return True if self.help(s) else False
        if len(point_sta) > 1 or (len(s) == 1 and s[0] == '.'):
            return False
        return True
    def help(self , s):
        num = "0123456789"
        sign = ["+" , "-"]
        for i in range(len(s)):
            if s[i] in num:
                continue
            if s[i] in sign and i != 0:
                return False
            if s[i] == '.':
                return False
            if s[i] == 'e':
                return False
        return True

if __name__ == "__main__":
    var = Solution()
    print(var.isNumber("+eo"))