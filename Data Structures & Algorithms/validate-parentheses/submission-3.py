class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Use list as stack
        # 1. Add: stack.append(..)
        # 2. Remove: stack.pop(..)
        # 3. Peak/Top: stack[-1]
        pairs = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in [")", "}", "]"]:
                if len(stack) == 0 or pairs[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0