class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        Each digit is its mapped value x 26*digit

        So we start by dividing by 26
            - value maps to first letter
            - remainer maps to the rest (the modulo btw)

            # digit = ord(c) - ord("A")
        '''
        def digToChar(digit: int) -> str:   
            # Function that converts a digit from 1 to 26 to A-Z
            return chr(digit + ord("A"))
        
        res = []
        while columnNumber > 0:
            # let's go backwards
            columnNumber -= 1
            curChar = columnNumber - ((columnNumber//26)*26)        # i believe this is the same as modulo?
            res.append(digToChar(curChar))
            # curChar was 25, which is 701-676
            columnNumber = columnNumber//26

        res.reverse()
        return ''.join(res)

            
        

