class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0
        # sort the numbers to avoid duplicates when considering "a"
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # check for duplicate values for "a"
            if i > 0 and a == nums[i-1]:
                continue

            # 2 pointer approach for 2 sum
            # while avoiding duplicates
            l, r = i+1, len(nums)-1
            while l < r:
                csum = a + nums[l] + nums[r]
                if csum < 0:
                    l += 1
                elif csum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # keep shifting until you elimnate duplicate values of "b"
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res