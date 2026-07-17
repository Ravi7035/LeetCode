from fractions import gcd
class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = number of elements divisible by d
        cnt = [0] * (mx + 1)

        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2

            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        # Prefix count of gcd values
        prefix = []
        values = []

        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []

        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans