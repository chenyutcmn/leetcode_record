import collections  
class Solution:
    def groupAnagrams(self, strs):
        ans = []
        dic = {}
        for item in strs:
            key = self.hash(item)
            print(key)
            if key not in dic:
                dic[key] = [item]
            else:
                dic[key].append(item)
        for _ , value in dic.items():
            ans.append(value)
        return ans

    def hash(self , string):
        string = sorted(string)
        res = ""
        for ch in string:
            res += ch
        return res
    

        


if __name__ == "__main__":
    var = Solution()
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(var.anagrams(test))
    #print(var.hash("bat"))