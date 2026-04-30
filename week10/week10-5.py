# week10-5.py 學習計畫 Binary Tree - DFS第四題
# LeetCode 437. Path Sum III
# 從上到下,有沒有一小段 「加起來是 targetSum」
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1 # 有1個上帝視角的0
        def helper(root, total): # 之前的total
            if root==None: return 0
            total += root.val
            ans = counter[total - targetSum] # 要先從counter抄到答案
            counter[total] += 1 # 累積多1個totoal (的斷點)
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            counter[total] -= 1 # 再扣掉
            return ans
        return helper(root, 0)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
