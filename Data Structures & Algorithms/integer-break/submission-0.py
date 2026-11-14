class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        break integer into at least 2 numbers, that have a huge product....

        Should always break into small parts, preferrably 3

        
        2 -> 1x1 = 1
        3 -> 2x1 = 2
        4 -> 2x2 = 4 (not 3x1)
        5 -> 2x3 = 6
        6 -> 3x3 = 9
        7 -> 3x2x2 = 3x4 = 12
        8 -> 3x3x2 = 18

        It looks like we shrink using the 3 method until it's either 4,2,0
        '''
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n % 3 == 0:      # ends with 0
            return int(3 ** (n/3))
        
        elif n % 3 == 2:    # ends up with 2 btw
            n -= 2
            return int((3 ** (n/3)) * 2)
        
        elif n % 3 == 1:    # end with 4
            n -= 4
            return int((3 ** (n/3)) * 4)
        