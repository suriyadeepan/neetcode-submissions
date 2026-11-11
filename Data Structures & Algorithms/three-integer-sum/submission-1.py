class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(start: int, end: int, target: int):
            lookup, res = set(), set()
            for i in range(start, end):
                key = -target - nums[i]
                pair = tuple(sorted((key, nums[i])))
                if key in lookup and pair not in res:
                    res.add(pair)
                else:
                    lookup.add(nums[i])
            return res

        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            pairs = twoSum(i+1, len(nums), nums[i])
            for pair in pairs:
                triplets.append([nums[i], *pair])


        return triplets
