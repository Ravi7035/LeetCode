class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        #sorting by end 
        intervals.sort(key=lambda x:x[1])
        
        previous_end=intervals[0][1]
        count=0

        for i in range(1,len(intervals)):
            
            if intervals[i][0] < previous_end:

                count+=1
            else:
                previous_end=intervals[i][1]

        return count
       

        