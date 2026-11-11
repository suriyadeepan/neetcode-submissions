class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for j in range(len(nums)):
            key = target - nums[j]
            if key in hm:
                return [hm[key], j]
            hm[nums[j]] = j