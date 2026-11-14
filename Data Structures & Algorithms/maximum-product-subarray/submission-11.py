class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = float('-inf')
        curpos = float('-inf')
        curneg = float('inf')

        for n in nums:
            if n == 0:
                curpos = float('-inf')
                curneg = float('inf')
                out = max(out, 0)
                continue

            oldpos, oldneg = curpos, curneg

            if n > 0:
                curpos = max(n, oldpos * n)
                curneg = min(n, oldneg * n)
            else:
                curpos = max(n, oldneg * n)
                curneg = min(n, oldpos * n)

            out = max(out, curpos)

        return out