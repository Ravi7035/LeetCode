class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start=0
        current_difference=0
        total_difference=0

        for i in range(len(gas)):

            current_difference+=gas[i]-cost[i]
            total_difference+=gas[i]-cost[i]

            if current_difference<0:
                start=i+1
                current_difference=0

        if total_difference>=0:
            return start

        else:
            return -1

      


        
        