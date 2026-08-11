"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we use minheap, then we pop the min, perform bs on keys of ending times
        # {ending_times: []}
        q = []
        for i in intervals:
            heapq.heappush(q, (i.start, i.end))
        d = collections.defaultdict(int)
        while q:
            curr_start, curr_end = heapq.heappop(q)
            #print(d)
            key = len(d.keys())
            a = sorted(d.keys())
            l, r = 0, len(a) - 1
            while l <= r:
                mid = (l + r)//2
                if curr_start >= a[mid]:
                    # move to right
                    key = mid
                    l = mid + 1
                else:
                    r = mid -1
            if key == len(d.keys()):
                d[curr_end] += 1
            else:
                d[curr_end] += 1
                d[a[key]] -= 1
                if d[a[key]] == 0:
                    del d[a[key]]
        
        return sum(d.values())

    