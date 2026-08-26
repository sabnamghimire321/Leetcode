class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                pointer = head

                while pointer is not slow:
                    pointer = pointer.next
                    slow = slow.next

                return pointer

        return None
