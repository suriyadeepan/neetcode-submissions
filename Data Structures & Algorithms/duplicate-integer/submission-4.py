class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash set
        # sacrific memory for time
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)

        return False