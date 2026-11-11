class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # def countChars(s: str) -> list[int]:
        #     count = [0] * 26
        #     for ch in s:
        #         count[ord(ch) - ord("a")] += 1
        #     return count

        # return countChars(s) == countChars(t)
        if len(s) != len(t): return False

        countS, countT = {}, {}
        for chs, cht in zip(s, t):
            countS[chs] = 1 + countS.get(chs, 0)
            countT[cht] = 1 + countT.get(cht, 0)
        
        print("countS", countS)
        print("countT", countT)

        for ch in countS:
            if countS[ch] != countT.get(ch, 0):
                return False

        return True