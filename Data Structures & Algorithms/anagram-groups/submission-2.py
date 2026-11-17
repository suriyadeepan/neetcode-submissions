class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # canonical key : list of anagrams
        for s in strs:
            # empty vector
            count = [0] * 26
            # map the word s
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            
            hm[tuple(count)].append(s)

        return list(hm.values())