from math import pow, log


class Solution(object):

    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        s = set([])
        LIMIT1 = 0 if x is 1 else int(log(bound, x))
        for i in range(0, LIMIT1 + 1):
            LIMIT2 = 0 if y is 1 else int(log(bound - pow(x, i), y))
            if bound - pow(x, i) < 0.99:
                break
            for j in range(0, LIMIT2 + 1):
                s.add(int(pow(x, i) + pow(y, j)))
                if y == 1:
                    break
        return list(s)
