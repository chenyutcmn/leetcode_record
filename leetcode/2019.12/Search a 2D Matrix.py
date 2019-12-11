class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if len(matrix) == 0:
            return False
        elif len(matrix) == 1:
            return self.help(matrix[0], target)
        else:
            mid = len(matrix) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if (mid + 1) == len(matrix):
                    return self.help(matrix[mid], target)
                else:
                    if matrix[mid][-1] < target:
                        return self.searchMatrix(matrix[mid+1:], target)
                    else:
                        return self.help(matrix[mid], target)
            elif matrix[mid][0] > target:
                if mid == 0:
                    return self.help(matrix[mid], target)
                else:
                    return self.searchMatrix(matrix[:mid], target)

    def help(self, row, target):
        if len(row) == 0:
            return False
        elif len(row) == 1:
            return True if row[0] == target else False
        else:
            mid = len(row) // 2
            print(mid)
            if row[mid] == target:
                return True
            elif row[mid] < target and (mid + 1) < (len(row)):
                return self.help(row[mid + 1:], target)
            elif row[mid] > target:
                return self.help(row[:mid], target)
            else:
                return False



var = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(var.searchMatrix(matrix, 19))