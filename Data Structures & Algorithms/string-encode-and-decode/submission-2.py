class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wlen = int(s[i:j])
            res.append(s[j+1:j+1+wlen])
            i = j + wlen + 1
        return res

