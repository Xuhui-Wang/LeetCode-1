import math


class Solution:
    # def __init__(self):
    #     self.n = 0
    #     self.flag = False
    #     self.start = 0

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points = sorted(points, key=lambda p: math.pow(p[0], 2) + math.pow(p[1], 2))
        return points[0: K]
