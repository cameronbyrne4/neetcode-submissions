class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        -- input: array of temperatures each day
        -- return array where, on each day, is the # of days before it gets warmer
        - (example: 2,1,3 --> 2,1,0)

        -- Brute force is O(n^2), literally just start at each day and go out until something is larger
        
        IDEA
        -- looking backwards, if a number is larger, they are the new blocker
        

        iterate over the temps
            While the stack is not empty and if the top temp is less than our current temp
            WE WANT THE CURRENT ONE TO SQUISH THE STACK DOWN 
            THAT WAY THE STACK IS SHAPED LIKE A PYRAMID
            AND WE UPDATE THE DISTANCE IT FELL TO SQUISH EACH CHILD
        
        '''

        # Days default at zero and theres one i for each day
        res = [0] * len(temperatures)
        stack = [] # pairs of i,t

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                # CRUSH IT
                # TOP FUCKING DIES
                topi, topt = stack.pop()
                res[topi] = i - topi

            stack.append((i,t))
        return res






