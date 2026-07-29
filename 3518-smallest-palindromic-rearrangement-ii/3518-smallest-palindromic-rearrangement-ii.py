class Solution(object):
    def smallestPalindrome(self, s, k):
        from collections import Counter
        from math import factorial

        freq = Counter(s)

        half = Counter()
        mid = ""

        for ch in sorted(freq):
            half[ch] = freq[ch] // 2
            if freq[ch] & 1:
                mid = ch

        m = sum(half.values())

        # factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        # Initial number of distinct permutations
        ways = fact[m]
        for v in half.values():
            ways //= fact[v]

        if k > ways:
            return ""

        left = []
        rem = m

        while rem:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                # permutations if ch is fixed here
                nxt = ways * half[ch] // rem

                if k <= nxt:
                    left.append(ch)
                    ways = nxt
                    half[ch] -= 1
                    rem -= 1
                    break
                else:
                    k -= nxt

        left = "".join(left)
        return left + mid + left[::-1]