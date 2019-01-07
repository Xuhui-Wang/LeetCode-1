class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search(self, r, v, ans):
    if r:
        if r.val is not v[self.start]:
            self.flag = True
            return
        self.start += 1
        if r.left and r.left.val is not v[self.start]:
            ans.append(r.val)
            search(self, r.right, v, ans)
            search(self, r.left, v, ans)
        else:
            search(self, r.left, v, ans)
            search(self, r.right, v, ans)


class Solution:
    def __init__(self):
        self.n = 0
        self.flag = False
        self.start = 0


    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.n = len(voyage)
        ans = []
        search(self, root, voyage, ans)

        return [-1] if self.flag else ans
