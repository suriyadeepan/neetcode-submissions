class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # maintain a number set
        # numSet = set(nums)
        # # max length of sequence
        # maxLen = 0

        # for n in nums:
        #     # check for start of a sequence
        #     if n-1 not in numSet:
        #         length = 0
        #         while n + length in numSet:
        #             # print(n+length, end=",")
        #             length += 1

        #         maxLen = max(maxLen, length)
            
        #     # print("\n")

        # return maxLen
        numSet = set(nums)
        maxLen = 0
        for n in nums:
            if n-1 not in nums:
                length = 0
                while (n + length) in numSet:
                    length += 1

                maxLen = max(maxLen, length)
        
        return maxLen
