# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        first = ListNode(0)
        temp = first

        while l1 is not None or l2 is not None:
            if l1 is None:
                num = l2.val
                l2 = l2.next
            elif l2 is None:
                num = l1.val
                l1 = l1.next
            else:
                num = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            if carry == 1:
                carry = 0
                num += 1
            if num >= 10:
                carry = 1
                num -= 10
            ln = ListNode(num)
            temp.next = ln
            temp = ln
        if carry == 1:
            temp.next = ListNode(1)
        return first.next
