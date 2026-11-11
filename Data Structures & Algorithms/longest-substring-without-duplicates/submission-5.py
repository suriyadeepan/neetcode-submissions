class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxlen = 0
        charSet = set()
        for ch in s:
            # keep removing from left until ch not in charSet
            while ch in charSet and left <= right:
                charSet.remove(s[left])
                left += 1
            # add ch to charSet
            charSet.add(ch)

            # update maxlen
            maxlen = max(maxlen, right - left + 1)

            if right < len(s):
                right += 1

        return maxlen

