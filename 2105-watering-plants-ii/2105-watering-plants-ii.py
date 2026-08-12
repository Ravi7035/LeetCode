class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        Initial_A = capacityA
        Initial_B = capacityB

        left = 0
        right = len(plants) - 1
        No_of_times = 0

        while left < right:

            # Alice
            if capacityA < plants[left]:
                capacityA = Initial_A
                No_of_times += 1

            capacityA -= plants[left]
            left += 1

            # Bob
            if capacityB < plants[right]:
                capacityB = Initial_B
                No_of_times += 1

            capacityB -= plants[right]
            right -= 1

        # Only one plant remains
        if left == right:

            if max(capacityA, capacityB) < plants[left]:
                No_of_times += 1

        return No_of_times