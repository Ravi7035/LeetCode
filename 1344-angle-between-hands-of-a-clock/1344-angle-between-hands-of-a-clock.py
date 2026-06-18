class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        first_angle=abs((30 *hour)-(5.5*minutes))
        second_angle=abs(360-first_angle)

        return min(first_angle,second_angle)