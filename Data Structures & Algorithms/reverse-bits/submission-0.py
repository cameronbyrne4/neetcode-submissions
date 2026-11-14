class Solution:
    def reverseBits(self, n: int) -> int:
        # read from one side, build on the other side of a new int
        # 32 bits, index 31 --> 0, 30 --> 1
        # new index = 31 - old index

        res = 0             # 0000000.
        for i in range(32):
            curBit = ((n>>i) & 1)       # check if the bit at index i is 1 (starting from right)
            if curBit:                  # Apply bit mask and OR from the left side
                res |= (1<<(31-i))


        return res