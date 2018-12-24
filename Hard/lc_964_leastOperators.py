from math import floor, log


class Solution(object):

    def leastOpsExpressTarget(self, x, target):
        cache = {}

        def dp(t):
            if t in cache:
                return cache[t]
            if t < x:
                ans = min(2 * t - 1, 2 * (x - t))
            else:
                d = floor(log(t) / log(x))
                f = x ** d
                m = floor(t / f)

                if m * f == t:
                    ans = min(m * d - 1, (x - m + 1) * d)
                else:
                    ans = min(dp(m * f) + 1 + dp(t - m * f),
                              dp((m + 1) * f) + 1 + dp((m + 1) * f - t))
            cache[t] = ans
            return ans

        return dp(target)
