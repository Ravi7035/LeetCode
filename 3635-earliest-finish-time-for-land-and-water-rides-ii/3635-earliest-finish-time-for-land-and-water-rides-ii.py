class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        
        land_end_time = []
        for s, d in zip(landStartTime, landDuration):
            land_end_time.append(s + d)
        land_end_time = sorted(land_end_time)

        water_end_time = []
        for s, d in zip(waterStartTime, waterDuration):
            water_end_time.append(s + d)
        water_end_time = sorted(water_end_time)

        res = float('inf')
        leet = land_end_time[0]
        for s, d in zip(waterStartTime, waterDuration):
            res = min(res, max(s, leet) + d)
        
        weet = water_end_time[0]
        for s, d in zip(landStartTime, landDuration):
            res = min(res, max(s, weet) + d)
        
        return res