class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for x in nums:
            if x-1 in numSet:
                continue

            count = 1
            while x+1 in numSet:
                x += 1
                count += 1
            
            longest = max(longest, count)
        
        return longest