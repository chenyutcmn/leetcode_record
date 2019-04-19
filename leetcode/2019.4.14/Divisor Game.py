class Solution:
    def divisorGame(self, N: int) -> bool:
        tabel = [False for _ in range(0 , N+1)]
        tabel[0] = None
        tabel[1] = False
        tabel[2] = True
        for i in range(3 , N+1):
            for j in range(1 , i):
                if i%j == 0 and tabel[i-j] == False:
                    tabel[i] = True
                    break
        return tabel[-1]

if __name__ == "__main__":
    var = Solution()
    print(var.divisorGame(4))