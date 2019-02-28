def get_longest_substring(s):
    count = 0
    start = 0
    length = len(s)
    hashmap = {}
    while (length - start) > count:
        print(start)
        oncecount = 0
        for i in range(start , length):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
                oncecount += 1
                print("this is oncecount")
                print(oncecount)
            else:
                print("this is count")
                print(count)
                start = hashmap[s[i]] + 1
                break
        count = max(count , oncecount)
        hashmap.clear()
    return count
            

        




if __name__ == "__main__":
    s = "bbbbb"
    print(get_longest_substring(s))