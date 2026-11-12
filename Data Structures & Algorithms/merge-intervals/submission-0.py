class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        intervals.sort(key = lambda i: i[0])
        
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            # to compare two intervals
            # expand to starts and ends
            s1, e1 = merged[-1]
            s2, e2 = intervals[i]
            # check for overlap
            if s2 <= e1:
                # check for largest end
                # edge case: [1, 5], [2, 4] => [1, 5]
                merged[-1] = [s1, max(e1, e2)]
            else:
                # just append interval: no overlap!
                merged.append([s2, e2])

        return merged
            

        
        