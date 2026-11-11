class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        def _count(s:str)->List[int]:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            return count
        
        for s in strs:
            count = tuple(_count(s))
            if count not in res:
                res[count] = []
            res[count].append(s)

        return list(res.values())