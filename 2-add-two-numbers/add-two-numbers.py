# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize dummy head of the result linked list
        dummy_head = ListNode(0)
        # Current node is the iterator for the result linked list
        current = dummy_head
        # Initialize carry to 0
        carry = 0

        # Loop through lists l1 and l2 until reaching the end of both
        while l1 or l2 or carry:
            # Extract values of the current nodes, if available
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of values and carry
            total = val1 + val2 + carry
            # Update carry for the next calculation
            carry = total // 10

            # Create a new node with the digit from the sum
            current.next = ListNode(total % 10)
            # Move to the next node in the result linked list
            current = current.next

            # Move to the next nodes in l1 and l2, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result linked list starting from the next node of dummy head
        return dummy_head.next
