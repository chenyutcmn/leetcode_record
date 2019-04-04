#第一版思路:暴力搜索整个状态空间
#改进思路:没有第二版了，他们全都是dfs

import numpy as np
def isValid(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    big = set()
    for i in range(9):
        for j in range(9):
            if board[i][j]!='.':
                cur = board[i][j]
                if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                    return False
                big.add((i,cur))
                big.add((cur,j))
                big.add((i/3,j/3,cur))
    return True

def findIndex(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == ".":
                resource = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
                col = data[i,:]
                row = data[:,j]
                cell = data[(i//3)*3:(i//3)*3+3 , (j//3)*3:(j//3)*3+3]
                for n in resource:
                    nn = str(n)
                    if (nn in col) or (nn in row) or (nn in cell):
                        resource.remove(n)
                return i , j , resource
    return -1
def solve(data):
    if findIndex(data) == -1 and isValid(data):
        return data
    if findIndex(data) == -1 and not isValid(data):
        return 0
    i , j , li= findIndex(data)
    if li == []:
        return 0
    else:
        temp = data.copy()
        for n in li:
            temp[i][j] = n
            if isValid(temp):
                res = solve(temp)
                if res != 0:
                    return res
    return 0
            

if __name__ == "__main__":
    var = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    test = np.array(var)
    print(solve(test))