"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# O(n.logn) time, O(n) space
# class Solution:
#     def canAttendMeetings(self, intervals: List[Interval]) -> bool:
#         intervals.sort(key=lambda i:i.start)
#         seen = []
#         for meeting in intervals:
#             if not seen or meeting.start >= seen[-1]:
#                 seen.append(meeting.end)
#             else:
#                 return False
#         return True

# O(n.logn) time, O(1) space
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True