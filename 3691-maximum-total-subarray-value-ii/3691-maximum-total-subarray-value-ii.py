class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
       
        import heapq


        n = len(nums)
        LOG = (n).bit_length()

        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            mx = [0] * (n - length + 1)
            mn = [0] * (n - length + 1)

            prev_max = st_max[j - 1]
            prev_min = st_min[j - 1]

            for i in range(n - length + 1):
                mx[i] = max(prev_max[i], prev_max[i + half])
                mn[i] = min(prev_min[i], prev_min[i + half])

            st_max.append(mx)
            st_min.append(mn)
            j += 1

        def value(l, r):
            length = r - l + 1
            p = length.bit_length() - 1

            mx = max(
                st_max[p][l],
                st_max[p][r - (1 << p) + 1]
            )

            mn = min(
                st_min[p][l],
                st_min[p][r - (1 << p) + 1]
            )

            return mx - mn

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)

            ans += -neg_val

            if r > l:
                nr = r - 1
                nv = value(l, nr)
                heapq.heappush(heap, (-nv, l, nr))

        return ans

        