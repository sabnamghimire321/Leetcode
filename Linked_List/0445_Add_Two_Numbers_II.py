class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_stack(node):
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack
            
        s1, s2 = to_stack(l1), to_stack(l2)
        carry = 0
        result = None
        
        while s1 or s2 or carry:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            
            total = x + y + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = result
            result = node
            
        return result
