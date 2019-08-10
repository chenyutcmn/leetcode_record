#对运行结果没有足够的预见性，导致改bug时间过多

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_list = [i+1 for i in range(n)]
        return self.help(num_list , k)
        
    def help(self , num_list , k):
        if len(num_list) == 1:
            return str(num_list[0])
        else:
            group = math.factorial(len(num_list) - 1)
            indx = (k // group) if (k % group == 0) else (k // group + 1)
            if indx == 0:
                new_list = num_list[1:]
            elif indx == len(num_list):
                new_list = num_list[:-1]
            else:
                new_list = num_list[:indx - 1] + num_list[indx:]
            return str(num_list[indx - 1]) + self.help(new_list , k - (indx - 1)*group)

if __name__ == "__main__":
    var = Solution()
    print(var.getPermutation(4 , 9))