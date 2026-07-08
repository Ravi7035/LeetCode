class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefValue = [0] * (n + 1)
        prefSum = [0] * (n + 1)
        cnt = [0] * (n + 1)

        for i in range(n):
            d = int(s[i])

            prefSum[i + 1] = prefSum[i]
            prefValue[i + 1] = prefValue[i]
            cnt[i + 1] = cnt[i]

            if d != 0:
                prefSum[i + 1] += d
                cnt[i + 1] += 1
                prefValue[i + 1] = (prefValue[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:

            digitSum = prefSum[r + 1] - prefSum[l]

            digits = cnt[r + 1] - cnt[l]

            value = (
                prefValue[r + 1]
                - prefValue[l] * pow10[digits]
            ) % MOD

            ans.append((value * digitSum) % MOD)

        return ans