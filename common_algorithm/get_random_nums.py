import random

def get_nums(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(1 , 100))

    return nums