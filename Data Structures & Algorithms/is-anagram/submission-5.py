class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def brute_force():
            # O(N.logN)
            return sorted(s) == sorted(t)

        def freq_equality():
            # O(N)
            if len(s) != len(t): return False
            fs, ft = {}, {}
            for i in range(len(s)):
                fs[s[i]] = fs.get(s[i], 0) + 1
                ft[t[i]] = ft.get(t[i], 0) + 1
            return fs == ft

        return freq_equality()