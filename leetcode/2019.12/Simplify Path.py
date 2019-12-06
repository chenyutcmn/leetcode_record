import collections
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = collections.deque(path.split('/'))
        output = []
        while len(paths) != 0:
            path = paths.popleft()
            if path == '' or path == '.':
                continue
            elif path == '..':
                if len(output) != 0:
                    output.pop()
            else:
                output.append(path)
        ans = '/'
        for path in output:
            ans += path
            ans += '/'
        return ans[:-1] if ans != '/' else ans
        


if __name__ == "__main__":
    test = Solution()
    print(test.simplifyPath('////////////////a//b////c/d//././/..'))