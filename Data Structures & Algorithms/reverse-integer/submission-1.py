class Solution:
    def reverse(self, x: int) -> int:
        # return 0 if ourside of the 32 bit integer range
        xAbs = abs(x)
        res = int(str(xAbs)[::-1])

        # Restore the negative if it was stripped
        if x < 0:
            res *= -1
        
        # We have properly reversed the number by now

        # Check for valid range
        if res < -(1 << 31) or res > 0x7FFFFFFF:
            return 0
        return res
        '''
        abs -> str -> reverse -> int -> neg.   ==*check range*==>
        '''
