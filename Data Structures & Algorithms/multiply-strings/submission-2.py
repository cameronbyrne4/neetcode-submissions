class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        How to multiply numbers elementary school style
        - big number over a single number
        - carry the tens digit (up to 81)

        Iterate over second number, sliding each time
            - do carries for additions yk


        '''
        out = 0

        num1 = int(num1)
        if num1 == 0 or int(num2) == 0:
            return str(0)

        shifter = 0
        for i in range(len(num2)):
            if shifter:
                out *= 10
            # go backwards thrui the secxond numberrrrrrrrrrrrrr
            out += num1 * int(num2[i])
            shifter = 1
            
        return str(out)





