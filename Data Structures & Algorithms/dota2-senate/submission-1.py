from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       
        '''
       - TLE using priority Q
       - Need to check if all in Q are the same, but that takes O(n), or would it be shorter as more and more are cancel?

       - Can use a size 2 array to check if each has been edited in the round
       ''' 
        stack = []
        q = deque()
        rd = [0] * 2
        n = len(senate)

        for i in range(n):
            q.append(senate[i])
            if q[-1] == "D":
                rd[0] = 1
            elif q[-1] == "R":
                rd[1] = 1
                

        while q:
            # We are done if we only added one of the them to the q
            if rd[0] != rd[1]:
                # What about when we add neither
                # Return the one that we DID add
                if rd[0] == 1:
                    return "Dire"
                else:
                    return "Radiant"
            rd[0], rd[1] = 0,0

            for _ in range(len(q)):
                cur = q.popleft()
                if (not stack) or (stack[-1] == cur):
                    stack.append(cur)
                    q.append(cur)
                    if q[-1] == "D":
                        rd[0] = 1
                    else:
                        rd[1] = 1
                else:
                    stack.pop() # top one is used up


    
