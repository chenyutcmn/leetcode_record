def get_res(strlist , num):
    res = ""
    diclist = []
    for i in range(num):
        dic = []
        diclist.append(dic)
    ptr = 0
    to_right = True
    to_left = False
    for indx , ch in enumerate(strlist , 0):
        diclist[ptr].append(ch)
        if to_right and ptr < (num - 1):
            ptr += 1
        elif to_left and ptr > 0:
            ptr -= 1
        if ptr == 0:
            to_right = True
            to_left = False
        if ptr == num - 1:
            to_right = False
            to_left = True
    print(diclist)
    for i in range(len(diclist)):
        for j in range(len(diclist[i])):
            res += (diclist[i][j])
    return res

if __name__ == "__main__":
    test = "PAYPALISHIRING"
    print(get_res(test , 3))
