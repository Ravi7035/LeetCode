class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf')
        for i in range(len(landStartTime)):
            land_end = landStartTime[i]+landDuration[i]
            for j in range(len(waterStartTime)):
                finish = max(land_end,waterStartTime[j])+waterDuration[j]
                ans = min(ans, finish)
        for i in range(len(waterStartTime)):
            water_end = waterStartTime[i]+waterDuration[i]
            for j in range(len(landStartTime)):
                finish = max(water_end,landStartTime[j])+landDuration[j]
                ans = min(ans,finish)
        return ans


            
        
        