class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        Can use 26 len array x 2

        One arr: tracks the first idx a letter appears
        Second arr: tracks the last idx a letter appears

        When we open up a substr:
            - track length of it
            - add new chars to a set
            - stop once we reach the last idx for all chars in set (in the substr)
                - could just track the max idx every time we add a guy, to be faster


        '''
        last = [-1] * 26
        res = []

        for i, c in enumerate(s):
            idx = ord(c)-ord('a')
            last[idx] = i
        
        curset = set()
        curset.add(s[0])
        curlast = last[ord(s[0])-ord('a')]
        curlen = 1

        for i in range(1, len(s)):
            # end case for the final one:
            
            # If idx is past curlast, we start a new everything
            print("Dbg - comparing i to curlast: ", i, curlast)
            if i > curlast:
                curset.clear()
                curset.add(s[i])
                curlast = last[ord(s[i])-ord('a')]
                res.append(curlen)
                curlen = 1
            # If not, need to append and update curlast and curlen and set
            else:
                curset.add(s[i])
                curlast = max(curlast, last[ord(s[i])-ord('a')])
                curlen += 1
            if i == len(s)-1:
                res.append(curlen)


        return res