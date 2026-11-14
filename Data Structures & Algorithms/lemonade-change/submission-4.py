class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10 = 0,0
        for b in bills:
            
            if b == 5:
                c5 += 1
                continue
            
            elif b == 10:
                # needs 5 in change
                if c5 == 0:
                    return False
                c5 -= 1
                c10 += 1    # give 5 take 10
            else:
                # needs 15 in change from whatever denom
                # try to prioritize the big one
                need = 15
                if c10 != 0:
                    need = 5
                    c10 -= 1    # give them a 10, they still need 5
                if c5 * 5 < need:
                    return False
                else:
                    # give back either 1 or 3 threes
                    c5 -= need//5
        return True