class Solution(object):
    def findMinArrowShots(self, points):
        count=1
        points.sort(key=lambda x:x[1])
        prev_end=points[0][1]


        for i in range(1,len(points)):

            if points[i][0] > prev_end:

                count+=1

                prev_end=points[i][1]        

        return count

        

