class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        cur = []

        def bt(start):
            if len(cur) == k:
                out.append(cur.copy())
                return

            for i in range(start, n + 1):
                cur.append(i)
                bt(i + 1)
                cur.pop()

        bt(1)
        return out