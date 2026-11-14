class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        -1 = size 1, moving left
        4 = size 4, moving right

        Goal: output arr of the surviving asteroids after collisions

        Idea: just use a stack

        STACKS: .append(), .pop(), [-1], len != 0
        '''

        asts = []

        for a in asteroids:
            if a > 0:
                asts.append(a)
                continue
            
            else:   # a < 0
                while len(asts)!=0 and asts[-1] > 0 and asts[-1] < -a:
                    # While top ast is moving right and smaller
                    asts.pop()  # top guy falls off

                # Either is empty, top moving left, or top not breakable
                if  len(asts)!=0 and asts[-1] == -a:  # Top same size --> both break
                    asts.pop()
                elif len(asts)!=0 and asts[-1] > -a:
                    continue
                    # no append
                else:
                    asts.append(a)
                
                # if the top is left we dont care
                # if top is right and smaller it DIES
                # if top is right and bigger we DIE
                # or if same we do both


        return asts

