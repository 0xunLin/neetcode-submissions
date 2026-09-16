"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        seen = []
        for meeting in intervals:
            if not seen or meeting.start >= seen[-1]:
                seen.append(meeting.end)
            else:
                return False
        return True