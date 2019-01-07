def reverse(A, s, e):
    while s < e:
        A[s], A[e] = A[e], A[s]
        s += 1
        e -= 1

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        ans = []
        for x in range(n, 0, -1):
            for i in range(n - 1, -1, -1):
                if A[i] == x:
                    if i:
                        ans.append(i)
                        reverse(A, 0, i - 1)
                        ans.append(i + 1)
                        reverse(A, 0, i)
                    break
        return ans
