class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def countChars(s: str) -> list[int]:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            return count

        return countChars(s) == countChars(t)
