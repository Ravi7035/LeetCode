class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        n = len(intervals)
        left, right = 0, n - 1
        pos = n   # default position if no overlap found

        # Binary search for first interval where end >= newInterval[0]
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][1] >= newInterval[0]:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1

        ans = []

        # Add intervals before overlapping position
        for i in range(pos):
            ans.append(intervals[i])

        # Merge overlapping intervals
        i = pos
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        # Add remaining intervals
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans