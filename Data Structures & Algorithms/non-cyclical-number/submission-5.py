class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            new = 0
            for digit in str(n):
                new += int(digit) * int(digit)
            n = new
        if n == 1:
            return True
        return False

