"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals)-1):
            start_1, end_1 = intervals[i].start, intervals[i].end
            start_2, end_2 = intervals[i+1].start, intervals[i+1].end
            if start_2 < end_1:
                return False

        return True

