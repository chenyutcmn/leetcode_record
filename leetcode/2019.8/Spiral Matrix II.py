##方案一
class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return []
        end = n**2
        if n % 2 == 1:
            temp = [[end]]
        else:
            temp = [[end-3 , end-2],[end , end-1]]
        print(temp)
        for i in range(len(temp)+2 , n+2 , 2):
            beg = end - i ** 2 + 1
            temp = self.help(temp , beg , i)
        return temp
    def help(self , temp , beg , n):
        top = [(beg+i) for i in range(n)]
        end = [(beg+3*n-3-i) for i in range(n)]
        for i in range(len(temp)):
            temp[i].insert(0 , beg+4*n-5-i)
            temp[i].append(beg+n+i)
        print(top)
        print(end)
        temp.insert(0 , top)
        temp.append(end)
        return temp

##方案二 更易于理解
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        row = col = count = 0
        size = n-1
        A = [[None for _ in range(n)] for _ in range(n)]
        
        for ith_num in range(1, n**2 + 1):
            if A[row][col]:
                row += 1; col += 1;
                count += 1; size -= 1
                
            A[row][col] = ith_num
            
            if row == count and col < size: col += 1
            elif row < size and col == size : row += 1
            elif row == size and col > count : col -= 1
            elif row > count and col == count: row -= 1
                
        return A
    
if __name__ == "__main__":
    var = Solution()
    print(var.generateMatrix(0))