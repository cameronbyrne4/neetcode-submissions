class Solution:
    def reverse(self, x: int) -> int:
        '''
        math problem? can we convert to str then char then int?
        '''
        # msut strip the neg at the start btw
        if x < 0:
            y = -x
        else:
            y = x
        s= str(y)
        n = len(s)
        
        reversed = 0
        for i in range(n-1,-1,-1):
            # going thru chars backwards boyyyy
            print(s, s[i])
            digit = int(s[i])
            reversed = reversed * 10 + digit
            if reversed < -(2**31) or reversed > 2**31-1:
                return 0

        
        if x < 0:
            reversed *= -1
        return reversed
        