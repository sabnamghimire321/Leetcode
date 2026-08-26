class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        geq_dummy = ListNode(0)

        less_tail = less_dummy
        geq_tail = geq_dummy

        node = head

        while node:
            nxt = node.next

            if node.val < x:
                less_tail.next = node
                less_tail = less_tail.next
            else:
                geq_tail.next = node
                geq_tail = geq_tail.next

            node = nxt

        geq_tail.next = None
        less_tail.next = geq_dummy.next

        return less_dummy.next
