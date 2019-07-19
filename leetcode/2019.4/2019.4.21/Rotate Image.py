class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.T(matrix)
        self.reverse(matrix)

    
    def T(self , mat):
        n = len(mat)
        for i in range(n):
            for j in range(i):
                mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
                
    def reverse(self , mat):
        n = len(mat)
        for i in range(n):
            mat[i].reverse()
            

if __name__ == "__main__":
    var = Solution()
    test = [[1,2,3],[4,5,6],[7,8,9]]
    var.rotate(test)
    print((test))