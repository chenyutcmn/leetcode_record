import get_random_nums

def insert_sort(nums):
    for i in range(1 , len(nums)):
        temp = nums[i]
        for j in range (0 , i)[::-1]:
            if temp >= nums[j]:
                nums[j+1] = temp
                break
            else:
                nums[j+1] = nums[j]
                if j == 0:
                    nums[0] = temp              #当前元素是本轮最小元素时，赋值
    return nums



if __name__ == "__main__":
    nums = get_random_nums.get_nums(20)
    print(nums)
    new_nums = insert_sort(nums)
    print(new_nums)