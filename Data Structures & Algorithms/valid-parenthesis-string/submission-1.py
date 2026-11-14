class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        maintain two stacks of the indices, lmao!
        '''
        so = [] # stack of open paren
        ss = [] # stack of stars

        for i,c in enumerate(s):
            if c == "(":
                so.append(i)
            elif c == "*":
                ss.append(i)
            else:   # ")"
                if len(so) > 0:     # closes the most recent open parenthesis
                    so.pop()
                elif len(ss) > 0:               # borrow help from star
                    ss.pop()
                else:
                    return False
        
        # chop that tree son
        while len(so) > 0 and len(ss) > 0 and ss[-1] > so[-1]:  # must have a star that is more recent
            so.pop()
            ss.pop()
        
        # Lets check if we failed to chop that tree....
        # Final checker up
        if len(so) == 0:
            return True
        return False