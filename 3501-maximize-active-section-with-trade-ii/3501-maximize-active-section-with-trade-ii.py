from bisect import bisect_left, bisect_right

class Solution(object):
    def build(self, idx, l, r, seg, arr):
        if l == r:
            seg[idx] = arr[l]
            return

        mid = (l + r) // 2
        self.build(2 * idx + 1, l, mid, seg, arr)
        self.build(2 * idx + 2, mid + 1, r, seg, arr)
        seg[idx] = max(seg[2 * idx + 1], seg[2 * idx + 2])

    def query(self, ql, qr, idx, l, r, seg):
        if l > qr or r < ql:
            return float("-inf")

        if ql <= l and r <= qr:
            return seg[idx]

        mid = (l + r) // 2
        return max(
            self.query(ql, qr, 2 * idx + 1, l, mid, seg),
            self.query(ql, qr, 2 * idx + 2, mid + 1, r, seg),
        )

    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        activeCount = s.count('1')

        blockStart = []
        blockEnd = []

        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                blockStart.append(start)
                blockEnd.append(i - 1)
            else:
                i += 1

        m = len(blockStart)

        if m < 2:
            return [activeCount] * len(queries)

        blockSize = [blockEnd[i] - blockStart[i] + 1 for i in range(m)]

        pairSum = [blockSize[i] + blockSize[i + 1] for i in range(m - 1)]
        N = len(pairSum)

        seg = [0] * (4 * N)
        self.build(0, 0, N - 1, seg, pairSum)

        ans = []

        for l, r in queries:
            low = bisect_left(blockEnd, l)
            high = bisect_right(blockStart, r) - 1

            maxPairSum = 0

            if low < high:
                firstLen = blockEnd[low] - max(blockStart[low], l) + 1
                lastLen = min(blockEnd[high], r) - blockStart[high] + 1

                if high - low == 1:
                    maxPairSum = firstLen + lastLen
                else:
                    pair1 = firstLen + blockSize[low + 1]
                    pair2 = blockSize[high - 1] + lastLen

                    rmq = 0
                    if low + 1 <= high - 2:
                        rmq = self.query(low + 1, high - 2, 0, 0, N - 1, seg)

                    maxPairSum = max(pair1, pair2, rmq)

            ans.append(activeCount + maxPairSum)

        return ans