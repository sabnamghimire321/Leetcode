from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        email_owner = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_owner:
                    union(i, email_owner[email])
                else:
                    email_owner[email] = i
                
        groups = defaultdict(list)
        for email, owner in email_owner.items():
            root = find(owner)
            groups[root].append(email)
            
        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
