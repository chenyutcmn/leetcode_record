def getres(strlist):
    reslist = []
    dicarray = []
    for i in range(len(strlist)):
        dic = {}
        for indx , ch in enumerate(strlist[i] , 0):
            if ch not in dic:
                dic[ch] = 1
            else: 
                dic[ch] += 1
        dicarray.append(dic)
    maxlen = 0
    maxlen_indx = 0
    for i in  range(len(dicarray)):
        length = len(dicarray[i])
        if length > maxlen:
            maxlen = length
            maxlen_indx = i
    commonnum_array = []

    for ch , num in dicarray[maxlen_indx].items():
        commonnum = num
        for j in range(len(dicarray)):
            if ch in dicarray[j]:
                if dicarray[j][ch] < commonnum:
                    commonnum = dicarray[j][ch]
            else:
                commonnum = 0
                break
        commonnum_array.append([ch , commonnum])
    
    for i in range(len(commonnum_array)):
        if commonnum_array[i][1] != 0:
            for j in range(commonnum_array[i][1]):
                reslist.append(commonnum_array[i])
    
    return reslist



if __name__ == "__main__":
    test = ["aaadcacb","adcbcadb","abbabdab","acbbabbb","ccaccccc","ccddcacd","cdaabccb","ccbdddcd"]
    print(getres(test))