# week09-6.py 學習計畫 Linked list 第2題
# LeetCode 328. Odd Even Linked List 偶數堆、奇數堆,串起來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] # 這題竟然可以用作弊法,  先轉換成陣列
        while head: # 逐一將Linked List 的值,放入陣列
            a.append( head.val)
            head = head.next # 記得換下一筆


        N = len(a) # 陣列的大小
        now = ans = ListNode() # 答案,有個None 右邊會塞真的 Nodes
        for i in range(0, N, 2):
            now.next = ListNode( a[i])
            now = now.next
        for i in range(1,N,2):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
