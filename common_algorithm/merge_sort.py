import get_random_nums

def merge(nums , left , right , mid):
    count_left = mid - left + 1
    count_right = right - mid
    count = right - left + 1
    L = [0] * count_left
    R = [0] * count_right
    lst = [0] * count
    k = 0
    for i in range(left , mid + 1):
        L[k] = nums[i]
        k += 1 

    k = 0
    for i in range(mid + 1 , right + 1):
        R[k] = nums[i]
        k += 1

    k = 0
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    
    if i < len(L):
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
    else:
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

    k = 0
    for v in range(left , right + 1):
        nums[v] = lst[k]
        k += 1


def merge_sort(nums , left , right):
    if(left < right):
        mid = (left + right) // 2
        merge_sort(nums , left , mid)
        merge_sort(nums , mid + 1 , right)
        merge(nums , left , right , mid)


if __name__ == "__main__":
    nums = get_random_nums.get_nums(26)
    print(nums)
    merge_sort(nums , 0 , 25)
    print(nums)
 
