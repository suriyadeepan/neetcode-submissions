class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = {0: 1}
        runningSum = 0
        total = 0

        for x in nums:
            runningSum += x
            reqPrefixSum = runningSum - k
            total += prefixSumCount.get(reqPrefixSum, 0)
            # add current runningSum
            prefixSumCount[runningSum] = prefixSumCount.get(runningSum, 0) + 1

        return total