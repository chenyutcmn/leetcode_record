def getres(strlist):
        if strlist == "":
            return ""
        dic = {}
        max_str = strlist[0]
        max_str_start = 0
        max_count = 1
        count = 0
        for indx , ch in enumerate(strlist , 0):
            if ch not in dic:
                dic[ch] = indx
            else:
                if max_str_start == 0 and max_count > 1:
                    
                count = indx - dic[ch] + 1
                if count > max_count:
                    max_str = strlist[dic[ch] : indx]
                    print(max_str)
                    max_count = count
                dic[ch] = indx
            print(count)
            print(dic)
        return max_str

if __name__ == "__main__":
    test = "babad"
    print(test[0:2])
    print(getres(test))