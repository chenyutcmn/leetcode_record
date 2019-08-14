class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = digits[::-1]
        num = 0
        for i in range(len(temp)):
            num += temp[i] * (10 ** i)
        num += 1
        num = str(num)
        ans = []
        for ch in num:
            ans.append(int(ch))
        return ans