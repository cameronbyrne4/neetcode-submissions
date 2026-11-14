class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        Should we just add using bits lol
        '''
        res = 0
        carry = 0

        # Do math from the back
        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            bitRes = bitA ^ bitB ^ carry
            res |= (bitRes << i)

            carry = bitA + bitB + carry > 1


        # fix negative values
        mask = 0xFFFFFFFF
        if res > 0x7FFFFFFF:        # 7 --> 0111
            res = ~(res ^ mask)

        return res