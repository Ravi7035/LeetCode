class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # Base: assume 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # Range where 1 move is enough
            diff[low] -= 1
            diff[high + 1] += 1

            # Exact sum where 0 moves needed
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        res = float('inf')
        curr = 0

        # Evaluate best possible sum
        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            res = min(res, curr)

        return res