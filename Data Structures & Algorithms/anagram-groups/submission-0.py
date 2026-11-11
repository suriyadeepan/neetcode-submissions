class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            charCount = [0] * 26

            for ch in s:
                charCount[ord(ch) - ord("a")] += 1
            
            res[tuple(charCount)].append(s)

        return list(res.values())
