class Solution:
    def fullJustify(self, words, maxWidth: int):
        ans = []
        line = []
        i = 0
        while i < len(words):
            word = words[i]
            line.append(word)
            if self.is_adapt(line , maxWidth):
                if i == (len(words) - 1):
                    ans.append(self.get_final_line(line , maxWidth))
                i += 1
            else:
                ans.append(self.get_line(line[:-1] , maxWidth))
                line = []
        return ans

    def is_adapt(self , words , maxWidth):
        if (self.len_of_words(words) + len(words) - 1) <= maxWidth:
            return True
        else:
            return False
    def get_line(self , words , maxWidth):
        line = ""
        spaces = maxWidth - self.len_of_words(words)
        if len(words) == 1:
            line += words[0]
            line += " " * (maxWidth - len(words[0]))
            return line
        each_base_space = spaces // (len(words) - 1)
        mod_space = spaces % (len(words) - 1)
        for i , word in enumerate(words):
            if i == (len(words) - 1):
                line += word
                return line
            line += word
            line += " " * each_base_space
            if i < mod_space:
                line += " "
            
    def get_final_line(self , words , maxWidth):
        line = ""
        for _ , word in enumerate(words):
            line += word
            line += " "
        line = line[:-1]
        line += " " * (maxWidth - len(line))
        return line
    def len_of_words(self , words):
        length = 0
        for _ , word in enumerate(words):
            length += len(word)
        return length

if __name__ == "__main__":
    var = Solution()
    print(var.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"] , 20))