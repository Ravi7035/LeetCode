class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        output=0
        max_end=0
        for start,end in intervals:

            if end > max_end:
                output+=1
                max_end=end

        return output

        
            
        