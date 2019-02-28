import get_random_nums
def sort(nums , left , right):
    temp = nums[left]
    while left < right:
        while left < right and nums[right] >= temp:
            right -= 1
        if left < right:
            nums[left] = nums[right]
        while left < right and nums[left] <= temp:
            left += 1
        if left < right:
            nums[right] = nums[left]    
    nums[left] = temp
    return left

def quick_sort(nums , left , right):
    if(left < right):
        index = sort(nums , left , right)
        quick_sort(nums , left , index - 1)
        quick_sort(nums , index + 1 , right)

if __name__ == "__main__":
    nums = get_random_nums.get_nums(10)
    print(nums)
    quick_sort(nums , 0 , 9)
    print(nums)