#深度优先还是广度优先，这是一个问题


class Solution:
    def exist(self, board, word: str) -> bool:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    temp = [[i, j]]
                    res.append(temp)
        if len(res) == 0:
            return False
        if len(word) == 1:
            return True
        else:
            for i, ch in enumerate(word[1:]):
                next = []
                for temp in res:
                    if len(temp) != (i + 1):
                        continue
                    else:
                        position = temp[-1]
                        chack = []
                        x, y = position[0], position[1]
                        if x > 0 and [x-1, y] not in temp:
                            chack.append([x-1, y])
                        if x < len(board)-1 and [x+1, y] not in temp:
                            chack.append([x+1, y])
                        if y > 0 and [x, y-1] not in temp:
                            chack.append([x, y-1])
                        if y < len(board[0])-1 and [x, y+1] not in temp:
                            chack.append([x, y+1])

                        for item in chack:
                            var = []
                            if board[item[0]][item[1]] == ch:
                                var = temp + [item]
                                next.append(var)
                                
                res = next
            if len(res) != 0:
                return True
            else:
                return False
                        

if __name__ == "__main__":
    var = Solution()
    test = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]
    print(var.exist(test, "AAB"))