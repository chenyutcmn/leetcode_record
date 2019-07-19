nums=[2,7,9,11,15]
target=20
res=[]

def get_indice(nums , target):
        retn = []
        for i in range(len(nums)):
                for j in range(i + 1 , len(nums)):
                        if (nums[i] + nums[j]) == target:
                               retn.append(i)
                               retn.append(j)
                               return retn
                        if (nums[i] + nums[j]) >target:
                                break


if __name__ == "__main__":
    res = get_indice(nums , target)
    print(res)


    