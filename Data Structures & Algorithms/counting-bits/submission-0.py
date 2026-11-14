class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(n+1):
            # implement same code as in the number of 1's problem
            count = 0
            for j in range(32):
                if (i >> j) & 1:
                    count += 1
            result[i] = count

        return result