class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = int(len(nums) * (len(nums) + 1) / 2)
        numsSum = sum(nums)
        return expectedSum - numsSum