class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen: dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for ch in s:
            if ch in closeToOpen:  # [1] closing paranthesis
                if stack and stack[-1] == closeToOpen[ch]:  # [1.1] Open exists on top
                    stack.pop() # pop top
                else:  # [1.2] Open does not exist
                    return False  # invalid
            else: # [2] opening paranthesis
                stack.append(ch)

        return len(stack) == 0 # stack is empty?
                