class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = {0: 1}
        sum, ans = 0, 0
        for num in A:
            sum += num
            _, sum_p = divmod(sum, K)
            cnt = m[sum_p] if sum_p in m else 0
            ans += cnt
            m[sum_p] = cnt + 1
        return ans
