#不允许用np，告辞 hhhhh
import numpy as np
class Solution:
    def isValidSudoku(self, board) -> bool:
        arr = np.array(board)
        print(arr)
        for i in range(9):
            col = arr[i , :]
            print(col)
            row = arr[: , i]
            print(row)
            dic = {}
            for n in col:
                if n != "." and (n not in dic):
                    dic[n] = 1
                elif n in dic:
                    return False
            dic = {}
            for n in row:
                if n != "." and (n not in dic):
                    dic[n] = 1
                elif n in dic:
                    return False
        for i in range(0 , 9 , 3):
            for j in range(0 , 9 , 3):
                dic = {}
                cell = arr[i:i + 3 , j:j + 3]
                for celli in cell:
                    for n in celli:
                        if n != "." and (n not in dic):
                            dic[n] = 1
                        elif n in dic:
                            return False
        return True

if __name__ == "__main__":
    var = Solution()
    test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(var.isValidSudoku(test))