#对树的遍历不够熟练
#另取余操作与哈希表的映射有关，大佬都这么写，我也学一下（虽然不知道为什么）
#在设计用除法来散射的哈希表时，我们都会用数值模哈希表大小，得到的余数来作为ID存入哈希表对应格子中。所有文章都表明要用一个较大的素数来作为哈希表的大小，也就是要模一个较大的素数。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        mod = int(1e9 + 7)
        self.ans = 0
        self.dfs(root , 0)
        return self.ans%mod
    def dfs(self , root , temp):
        if root.left == None and root.right == None:
            self.ans = self.ans + (temp*2 + root.val)
        else:
            if root.left:
                self.dfs(root.left , temp*2 + root.val)
            if root.right:
                self.dfs(root.right , temp*2 + root.val)
        