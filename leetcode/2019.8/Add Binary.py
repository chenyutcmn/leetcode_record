class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dic = {(1 , 1 , 1) : '11' , (1 , 0 , 1) : '10' , (0 , 1 , 1) : '10' , (0 , 0 , 1) : '01' , (1 , 1 , 0) : '10' , (1 , 0 , 0) : '01' , (0 , 1 , 0) : '01' , (0 , 0 , 0) : '00'}
        dic1 = {(1 , 1) : '10' , (1 , 0) : '01' , (0 , 1) : '01' , (0 , 0) : '00'}
        m = len(a)
        n = len(b)
        ans = ''
        y = 0
        s = ''
        if m > n:
            s = a[:m - n]
            temp1 = a[m - n:]
            temp2 = b
        elif m < n:
            s = b[:n - m]
            temp1 = a
            temp2 = b[n - m:]
        else:
            temp1 = a
            temp2 = b
        for i in range(len(temp1) - 1 , -1 , -1):
            add = (int(temp1[i]) , int(temp2[i]) , y)
            y = int(dic[add][0])
            ans += dic[add][1]
        for i in range(len(s) - 1 , -1 , -1):
            add = (int(s[i]) , y)
            print(add)
            print(dic1[add])
            added = dic1[add][1]
            print(added)
            y = int(dic1[add][0])
            ans += added
        if y == 1:
            ans += '1'
        return ans[::-1]


if __name__ == "__main__":
    var = Solution()
    print(var.addBinary("101111" , "10"))