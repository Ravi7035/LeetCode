class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        from bisect import bisect_right
        def solve(firstStart, firstDur, secondStart, secondDur):

            rides = sorted(zip(secondStart, secondDur))
            starts = [s for s, d in rides]

            n = len(rides)

            prefixMinDur = [0] * n
            prefixMinDur[0] = rides[0][1]

            for i in range(1, n):
                prefixMinDur[i] = min(prefixMinDur[i - 1],
                                      rides[i][1])

            suffixMinFinish = [0] * n
            suffixMinFinish[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suffixMinFinish[i] = min(
                    suffixMinFinish[i + 1],
                    rides[i][0] + rides[i][1]
                )

            ans = float('inf')

            for s, d in zip(firstStart, firstDur):
                end_time = s + d
                pos = bisect_right(starts, end_time) - 1
                if pos >= 0:
                    ans = min(ans,
                              end_time + prefixMinDur[pos])
                if pos + 1 < n:
                    ans = min(ans,
                              suffixMinFinish[pos + 1])
            return ans

        return min(
            solve(landStartTime, landDuration,
                  waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)
        )