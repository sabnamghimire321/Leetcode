class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while has_k_nodes(group_prev.next, k):
            curr = group_prev.next
            prev = None

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tail = group_prev.next
            group_prev.next = prev
            tail.next = curr
            group_prev = tail

        return dummy.next
