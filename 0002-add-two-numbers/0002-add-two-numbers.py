# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode(0)
        temp = l3
        num1 = l1.val
        num2 = l2.val
        i=1
        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                num1 += (10**i) * l1.val
            if l2.next:    
                l2 = l2.next
                num2 += (10**i) * l2.val
            i += 1
        print (num1, num2)
        total = str(num1 + num2)
        temp.val = int(total[-1])
        for digit in total[-2::-1]:
            temp.next = ListNode(int(digit))
            temp = temp.next
        return l3