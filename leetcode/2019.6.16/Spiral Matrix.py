class Solution:
    def spiralOrder(self, matrix):
        return self.help(matrix)
    
    def help(self , mat):
        if len(mat) == 0:
            return []
        elif len(mat) == 1:
            return mat[0]
        elif len(mat[0]) == 0:
            return []
        elif len(mat[0]) == 1:
            res = []
            for i in range(len(mat)):
                res.append(mat[i][0])
            return res
        else:
            ans = []
            for i in range(len(mat)):
                if i == 0:
                    ans += mat[0]
                    
                elif i == len(mat) - 1:
                    mat[i].reverse()
                    print(mat[1:])
                    ans += mat[i]
                    for j in range(len(mat)-2 , 0 , -1):
                        ans.append(mat[j][0])
                else:
                    ans.append(mat[i][-1])
            new_mat = []
            print(ans)
            for i in range(1 , len(mat) - 1):
                new_mat.append(mat[i][1 : -1])
            print(new_mat)
            return ans + self.help(new_mat)

if __name__ == "__main__":
    var = Solution()
    print(var.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
            