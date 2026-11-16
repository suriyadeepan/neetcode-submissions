class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            
            i += 1

            word = ""
            for _ in range(int(count)):
                word += s[i]
                i += 1

            res.append(word)
        
        return res

            
            



            
