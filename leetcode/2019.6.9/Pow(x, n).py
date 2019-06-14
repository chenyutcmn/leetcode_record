import collections
class Solution(object):
    def myPow(self, x, n):
        if n > 0:
            x = x
        elif n < 0:
            n = -n
            x = 1/x
        else:
            return 1
        stack = collections.deque()
        while n > 1:
            if n % 2 == 1:
                stack.append(x)
            n = n // 2
            x = x * x
        while len(stack) != 0:
            x = x * stack.pop()
        return x
if __name__ == "__main__":
    print("test")
    var = Solution()
    print(var.myPow(2,-2))