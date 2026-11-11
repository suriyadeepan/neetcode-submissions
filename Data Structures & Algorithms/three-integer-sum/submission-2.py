class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(start: int, end: int, target: int):
            lookup, res = set(), set()
            for i in range(start, end):
                key = target - nums[i]
                pair = tuple(sorted((key, nums[i])))
                if key in lookup and pair not in res:
                    res.add(pair)
                else:
                    lookup.add(nums[i])
            return res

        def twoSum2P(nums: List[int], l: int, r: int, target: int):
            # assumes nums->sorted array
            pairs = []
            while l < r:
                csum = nums[l] + nums[r]
                if csum == target:
                    pairs.append((nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif csum < target:
                    l += 1
                else:
                    r -= 1

            return pairs



        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # pairs = twoSum(i+1, len(nums), nums[i])
            pairs = twoSum2P(nums, i+1, len(nums)-1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i], *pair])


        return triplets
