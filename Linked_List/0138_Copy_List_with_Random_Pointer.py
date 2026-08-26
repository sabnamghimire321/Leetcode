class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next
            
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
            
        node = head
        copy_head = head.next
        while node:
            copy = node.next
            node.next = copy.next
            copy.next = copy.next.next if copy.next else None
            node = node.next
            
        return copy_head
