class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
 
        def is_valid_segment(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255
 
        def backtrack(start):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for length in range(1, 4):
                segment = s[start:start+length]
                if not segment or not is_valid_segment(segment):
                    continue
                path.append(segment)
                backtrack(start + length)
                path.pop()
 
        backtrack(0)
        return result
