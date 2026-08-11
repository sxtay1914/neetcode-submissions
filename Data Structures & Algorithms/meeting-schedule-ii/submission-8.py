"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # store the room with earliest ending time
        intervals.sort(key=lambda x: x.start)
        q = []
        for i in intervals:
            if q and i.start >= q[0]:
                # when do we need to pop it out?
                heapq.heappop(q)
            heapq.heappush(q, i.end)
        return len(q)