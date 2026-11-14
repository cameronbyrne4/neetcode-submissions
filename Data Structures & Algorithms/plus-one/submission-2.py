class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #i = len(digits)-1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
                # CASE 1 COMPLETE

            # if the digit is 9
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                return digits
            
                # not 9? we done
            

        # In case the last one is 9
        
        #return digits



        # Case 1 - last one isnt 9
            # Increment by 1 and return it
        # Case 2 - it is 9:
            # turn to zero and increment the next one by 1
                # case 1