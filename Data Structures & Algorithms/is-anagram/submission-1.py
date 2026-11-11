class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count_(chars: str):
            hm = {}
            for ch in chars:
                if ch not in hm:
                    hm[ch] = 0
                hm[ch] += 1
            return hm

        return count_(s) == count_(t)
