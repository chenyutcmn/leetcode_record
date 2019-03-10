#堆排序的应用

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pos = []
        neg = []
        zero = 0
        for num in A:
            if num == 0:
                zero += 1
            if num > 0:
                pos.append(num)
            if num < 0:
                neg.append(num)
        pos.sort(reverse = True)
        neg.sort()
        n = len(pos)
        m = len(neg)
        if K < m:
            print("K<M")
            print(neg[0:K])
            return sum(pos) - sum(neg[0:K]) + sum(neg[K:])
        if K >= m:
            print("K>M")
            if zero != 0:
                return sum(pos) - sum(neg)
            else:
                if (K - m) % 2 != 0:
                    return sum(pos[:-1]) - sum(neg) - pos[-1]
                else:
                    return sum(pos) - sum(neg)


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heapq.heapify(A)
        for i in range(K):
            p = heapq.heappop(A)
            if p == 0:
                break
            heapq.heappush(A, -p)
        return sum(A)