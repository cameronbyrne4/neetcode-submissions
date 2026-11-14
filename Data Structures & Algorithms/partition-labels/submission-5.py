class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        input = str
        -- split into as many as a we can (big n list)
        -- RULE: each letter appears in only oen substring
        -- each element in return list is the size of substring in the order they appear

        brute force: try every combination of strings like 2^n

        Notes:
        - each character has a first and last appearance index
        - every time we start one, we have to finish it
        - we can't finish it if there are other open ones inside!
        -- so number open == number finished

        # we can find the first and last by iteratig forwards and backwards or just once

        # Solution!!!
        '''
        res = []
        
        g = {}
        for i, c in enumerate(s):
            g[c] = i
        # stores the last index each character pops up

        endi = 0      # end index is the last index of the first char
        cursize = 0
        for i in range(len(s)):
            endi = max(endi, g[s[i]])
            cursize += 1

            # End conditions
            if endi == i:
                res.append(cursize)
                # DONT EVEN BOTHER RESETTING ENDI
                cursize = 0
            '''
            Start counting up, noting the max idx of each elem

            If we ever reach it, we can append and reset and go next
            '''



        return res
    

