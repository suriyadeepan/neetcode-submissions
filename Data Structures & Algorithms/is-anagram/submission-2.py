class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count_(s: str) -> List[int]:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            return count

        return count_(s) == count_(t)
