class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        Total_Mass=mass
        for i in range(len(asteroids)):
            if Total_Mass>=asteroids[i]:
                Total_Mass+=asteroids[i]
            else:
                return False

        return True
        