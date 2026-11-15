class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSumCount = {0: 1} # seen 0 once before array starts
        runningSum = 0
        total = 0

        for x in nums:
            runningSum += x
            # Check for prefix
            preSum = runningSum - k
            total += preSumCount.get(preSum, 0)
            # add current element as prefix
            preSumCount[runningSum] = preSumCount.get(runningSum, 0) + 1

        return total