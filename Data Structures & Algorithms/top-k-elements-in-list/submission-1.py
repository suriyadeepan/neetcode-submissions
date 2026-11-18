class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solve by bucket sort
        # using frequency bucket
        freqBuckets = [[] for _ in range(len(nums) + 1)]

        # get count of chars
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # fill in the buckets
        for num, f in count.items():
            freqBuckets[f].append(num)

        # find top k element by iterating from right
        topK = []
        for i in range(len(freqBuckets)-1, -1, -1):
            for num in freqBuckets[i]:
                topK.append(num)
                if len(topK) == k:
                    return topK
        