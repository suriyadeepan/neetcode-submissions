import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def verifySpeed(k: int):
            rsum = 0
            for p in piles:
                rsum += math.ceil(p/k)
            return rsum <= h

        l, r = 1, max(piles)
        # [0, 1, 2, ... max(piles)]
        k = r
        while l <= r:

            mid = (l + r)//2
            speedOk = verifySpeed(mid)
            if speedOk:
                # update best k
                k = min(k, mid)
                # move left looking for smaller k
                r = mid - 1
            else: # not fast enough, move right
                l = mid + 1

        return k