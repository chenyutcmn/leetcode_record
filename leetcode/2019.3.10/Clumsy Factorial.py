#eval()函数计算表达式的值

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        listN = list(range(1 , N + 1))
        listN.reverse()
        if len(listN) < 5:
            return self.getOneRes(listN , 0 , N)
        k = len(listN) % 4
        res = self.getOneRes(listN , 0 , 4)
        print(res)
        for i in range(4, len(listN) - k , 4): 
            print(i)
            res -= self.getOneRes(listN , i , 4)
            print(res)
        if k == 1:
            res -= listN[-1]
        if k == 2:
            res -= (listN[-1] * listN[-2])
        if k == 3:
            res -= ((listN[-3] * listN[-2]) //listN[-1])
        return res
    def getOneRes(self , listN , i , j):
        if j == 4:
            return (listN[i] * listN[i + 1]) // listN[i + 2] + listN[i + 3]
        elif j == 0:
            return 0
        elif j == 1:
            return listN[i]
        elif j == 2:
            return listN[i] * listN[i + 1]
        elif j == 3:
            return (listN[i] * listN[i + 1]) // listN[i + 2]


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = []
        o = ['*', '//', '+', '-']
        k = 0
        for i in range(N, 0, -1):
            s.append(str(i))
            s.append(o[k])
            k = (k + 1) % 4
        s.pop()
        return eval(''.join(s))