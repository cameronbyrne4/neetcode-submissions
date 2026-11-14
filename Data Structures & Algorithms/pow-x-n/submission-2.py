class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if n < 0:
            x = 1 / x
            n = n * -1
        res = x
        for i in range(n-1):
            res = res * x


        return res