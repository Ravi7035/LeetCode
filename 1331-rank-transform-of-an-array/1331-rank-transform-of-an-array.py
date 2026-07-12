class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp = sorted(arr)

        rank = {}
        curr = 1

        for num in temp:
            if num not in rank:
                rank[num] = curr
                curr += 1

        ans = []
        for num in arr:
            ans.append(rank[num])

        return ans