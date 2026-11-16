class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: # == ]
                # get the substring inside the brackets
                substring = ""
                while stack[-1] != "[":  # top -x-> [
                    substring = stack.pop() + substring
                # the loop above gets all the chars within the brackets
                # now we are at "["
                # lets pop it off
                stack.pop()

                # similar method to get the integer substring
                k = ""
                # loop till you see non-int
                # ensure stack isn't empty => why?
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # now we have k
                # expand the substring by k and add to stack
                stack.append(int(k) * substring)

        return "".join(stack)