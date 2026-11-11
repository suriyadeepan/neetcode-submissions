class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            # check for duplicates
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # add character to right to the set
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res
        
