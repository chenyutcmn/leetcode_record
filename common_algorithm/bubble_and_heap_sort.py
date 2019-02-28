import random

def exchange(x , y):
    z = x
    x = y
    y = z
    return x,y

def bubble(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = exchange(nums[j],nums[j+1])
    return nums


def adjust(nums , start , size):
    lchild = start*2+1
    rchild = start*2+2
    heap_top = start
    if start < size//2:
        if nums[lchild] > nums[heap_top]:                               #一定会有左子树
            heap_top = lchild
        if rchild < size and nums[rchild] > nums[heap_top]:             #没有右子树的情况
            heap_top = rchild
        if heap_top != start:
            nums[heap_top] , nums[start] = nums[start] , nums[heap_top]
            adjust(nums , heap_top , size)

def build_heap(nums):
    for i in range(0 , len(nums) >> 1)[::-1]:           #从有子节点的最后一个节点开始往前遍历
        adjust(nums , i , len(nums))
    print("this is builed heap")
    print(nums)

def heap_sort(nums):
    sorted_nums = []
    build_heap(nums)
    for i in range(0 , len(nums))[::-1]:
        sorted_nums.append(nums[0])
        nums[0],nums[i] = nums[i],nums[0]
        adjust(nums , 0 , i-1)                          #交换待排序数和对顶元素，调整堆,调整范围(0,i-1)
    return sorted_nums                    


if __name__ == "__main__":
    nums = []
    for i in range(20):
        nums.append(random.randint(1 , 50))
    print(nums)
    new_nums = heap_sort(nums)
    print (new_nums)
