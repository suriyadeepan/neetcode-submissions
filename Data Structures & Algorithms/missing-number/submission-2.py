class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        missingNum = -sum(nums) + int(maxNum * (maxNum+1)/2)
        if missingNum == 0 and maxNum == len(nums)-1:
            return maxNum + 1

        return missingNum
