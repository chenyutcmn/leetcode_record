class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cout = 0
        while len(s) != 0:
            if s[-1] == " ":
                s = s[:-1]
            else:
                break
        if len(s) == 0:
            return 0
        for i in range(len(s) - 1 , -1 , -1):
            if s[i] != ' ':
                cout += 1
            else:
                return cout
        return cout
        
if __name__ == "__main__":
    var = Solution()
    print(var.lengthOfLastWord("a               "))